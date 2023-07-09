from flask import Blueprint
from app.services.users.register import register,test_token
from app.services.users.login import login


routes = Blueprint('register', __name__)

routes.add_url_rule('/register', methods=['POST'], view_func=register)
routes.add_url_rule('/login', methods=['POST'], view_func=login)
routes.add_url_rule('/test', methods=['POST'], view_func=test_token)
