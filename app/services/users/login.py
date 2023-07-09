from flask import request
from app.models.users import User
import time, jwt

def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    print(email,password,data)
    existing_user = User.query.filter_by(email=email).first()

    if not existing_user or not existing_user.check_password(password):
        return {'message': 'Invalid email or password', 'status': False}


    return {
        "message": 'Login successful.',
        "status": True,
        "data": {
            "token": generate_token(existing_user.id),
            "user": existing_user.email
        }
    }


def generate_token(id):
    token = {
        'iss': 'https://localhost:5000',
        'iat': time.time(),
        'data': {
            'user': {
            'id': id
            }
        }
    }

    return jwt.encode(token, "rU!41g|1Lk#GTV[:Fx5aho+~Ygd`<gZ|Pf{p2);+?i#Fg3F)7(yaJ<yN|lp(b-hU", algorithm="HS256")