import datetime
import os
# import yaml
from flask import request
from flask_restful import Api, Resource
from sqlalchemy import exc
import sqlalchemy.exc as sqlalchemy_exc
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from config import db
from usersmicroservice.models.users import Users
from usersmicroservice.schema import *






class GetAddUsers(Resource):
    def __init__(self):
        pass
    # get all users

    def get(self):
        try:
            user_id = request.headers.get('userid')
            obj = Users.query.filter(Users.id != user_id).order_by(Users.id).all()
            if obj:
                schema = UsersSchema(many=True)
                data = schema.dump(obj).data
                response = {
                    "success": True, "message": "data fetched succeessfully", "data": data}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in users"}
                return(response)
        except Exception as e:
            return({"success": False, "error_message": "server is down try after sometime", "error": str(e)})

    # post users
    def post(self):
        try:
            request_json_object = request.get_json()
            request_json_object['password'] = generate_password_hash(
                request_json_object['password'])
            schema = AddUserSchema()
            new_user_obj = schema.load(
                request_json_object, session=db.session).data
            db.session.add(new_user_obj)
            db.session.commit()
            data = schema.dump(new_user_obj).data
            user_response = {
                "success": True, "message": "User registered succeessfully", "data": data}
            return (user_response)
        except KeyError as e :
            return({"success": False, "message": "Incorrect key name", "error":str(e.args)})
        except exc.IntegrityError as e:
            errorInfo = e.orig.args
            message=errorInfo[1]
            return({"success": False, "message": message})
        except sqlalchemy_exc.SQLAlchemyError as e:
            return({"success": False, "message":str(e.args)})
        except Exception as e:
            return({"success": False, "message": str(e.args)})






# user sign in api call
class Signin(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            request_json_data = request.get_json()
            email = request_json_data['email']
            password = request_json_data['password']
            email_check = db.session.query(Users).filter(
                Users.email == email).first()
            if email_check is not None:
                schema = UsersSchema()
                data = schema.dump(email_check).data
                hashed_password = email_check.password
                if check_password_hash(hashed_password, password):
                    success_response = {
                        "success": True, 'data': data, 'message': 'User logined successfully'}
                    return(success_response)
                else:
                    password_response = {"success": False,
                                         "message": "Invalid password"}
                    return(password_response)
            else:
                username_response = {"success": False,
                                     "message": "Invalid UserName"}
                return(username_response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e)})



class GetUpdateUser(Resource):
    def __init__(self):
        pass

    # users get call based on id
    def get(self, id):
        try:
            user = Users.query.filter(Users.id == id).one_or_none()
            if user is not None:
                user_schema = UsersSchema()
                data = user_schema.dump(user).data
                user_response = {"success": True, "message":"data fetched successfully", "data": data}
                return (user_response)
            else:
                response = {"success": False, "message": "no data found on this id", "id": id}
                return(response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e)})



    
