from app.services.belbo_api.belvoConn import configure_belvo
from app.utils.check_session import check_session
from app.models.users import Bank,User
from config.db import db
from flask import request
import hashlib

belvoClient = configure_belvo()


@check_session(required=[],returnID=True)
def register_bank(idUser):
    data = request.get_json()

    response = belvoClient.Links.create(institution=data.get("institution"),
                                    username=data.get("username"),
                                    password=data.get("password"),
                                    external_id= hash_id(idUser)
    )
    if isinstance(response,dict):
        new_bank = Bank(institution=response['institution'],
                        status=response['status'],
                        link=response['id'],
                        created_at=response['created_at'],
                        user_id=idUser)
        db.session.add(new_bank)
        db.session.commit()
    
        return {"message":"Bank added successfully","status":True}
    else:
        message = response[0]['message']
        return {"message": f"Something went wrond adding the bank. Please Try Again.{message}"}


@check_session(required=[])
def delete_bank():
    data = request.get_json()
    belvoClient.Links.delete(data['link'])
    link = Bank.query.filter_by(link=data['link']).first()

    db.session.delete(link)
    db.session.commit()
 
    return {"message":"Bank deleted successfully","status":True}


@check_session(required=[],returnID=True)
def list_all_banks(idUser):

    user_banks = [{"name":bank['institution'],
                   "last_access":bank['last_accessed_at'],
                   "status":bank['status'],
                   "link":bank['id']
                   } for bank in belvoClient.Links.list(external_id=hash_id(idUser))]
    

    return {"data":user_banks}


@check_session(required=[])
def get_account():
    data = request.get_json()

    # Retrieve accounts
    accounts = belvoClient.Accounts.create(
    link=data['link']
    )
    return {"message":"Account Info","data":accounts,"status":True}


@check_session(required=[])
def get_transactions():
    data = request.get_json()
    # Retrieve transactions
    transactions = [{"name":x['merchant']['name'],
                "amount":x['amount'],
                "currency":x['currency'],
                "reference":x['reference'],
                "status":x['status'],
                "category":x['category'],
                "type":x['type'],
                } for x in belvoClient.Transactions.create(
                                                    link=data['link'],
                                                    date_from=data['date_from'],
                                                    date_to=data['date_to']
                                                    )]
    print(transactions[0]['amount'])
    return {"message":"Transactions Info","data":transactions,"status":True}


def hash_id(id):
    id_bytes = str(id).encode('utf-8')
    hash_result = hashlib.sha256(id_bytes).hexdigest()
    return hash_result
