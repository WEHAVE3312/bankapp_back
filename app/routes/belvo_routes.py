from flask import Blueprint
from app.services.belbo_api.belvo_requests import register_bank,delete_bank,list_all_banks, get_account,get_transactions


routes = Blueprint('belvo', __name__)

routes.add_url_rule('/add', methods=['POST'], view_func=register_bank)
routes.add_url_rule('/delete', methods=['DELETE'], view_func=delete_bank)
routes.add_url_rule('/get/banks', methods=['GET'], view_func=list_all_banks)
routes.add_url_rule('/get/account', methods=['GET'], view_func=get_account)
routes.add_url_rule('/get/transactions', methods=['POST'], view_func=get_transactions)

