from app.models.users import User
import jwt
from flask import request
from functools import wraps

def check_session(required = [], returnID = False):
    def check_privileges_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x_api_key = request.headers.get('x-api-key')
            if not x_api_key:
                return { "message":"You have no permission for this action. Not Access Token", "status": False }
            else:
                try:
                    decoded = jwt.decode(x_api_key, "rU!41g|1Lk#GTV[:Fx5aho+~Ygd`<gZ|Pf{p2);+?i#Fg3F)7(yaJ<yN|lp(b-hU", algorithms="HS256")
                except:
                    return { "message":"You have no permission for this action. Invalid Token", "status": False }
        
            if decoded.get("iss") != 'https://localhost:5000':
                return { "message":"You have no permission for this action. Not iss", "status": False }
      
            user_id = decoded.get("data").get("user").get("id")
            if not user_id:
                return {"message":"You have no permission for this action. Invalid Token", "status": False}
      
            user = User.query.filter_by(id=user_id).first()

            if not user:
                return {"message":"You have no permission for this action. User Not Exists", "status": False}
      
            if returnID:
                kwargs["idUser"] = user_id
            return func(*args, **kwargs)
        return wrapper
    return check_privileges_decorator