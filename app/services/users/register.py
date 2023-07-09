from flask import request
from app.models.users import User
from werkzeug.security import generate_password_hash
from config.db import db
from app.utils.check_session import check_session


def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return {'message': 'Email already registered', 'status': False}
    
    new_user = User(email=email,password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    print(email, generate_password_hash(password))
    return {"message":"User Registered succesfully","status": True}

@check_session(required=[],returnID=True)
def test_token(idUser):
    return {"message":idUser}