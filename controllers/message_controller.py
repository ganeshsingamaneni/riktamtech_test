import datetime
import os
# import yaml
from flask import request
from flask_restful import Api, Resource
from sqlalchemy import exc
import sqlalchemy.exc as sqlalchemy_exc
from config import db
from models.messages import Messages
from schemas.messageschema import *

from sqlalchemy import or_,and_





class GetAddMessages(Resource):
    def __init__(self):
        pass
    # get all Groups

    def get(self):
        try:
            Group_id = request.headers.get('group_id')
            obj = Messages.query.filter(Messages.id != Group_id).order_by(Messages.id).all()
            if obj:
                schema = MessagesSchema(many=True)
                data = schema.dump(obj).data
                response = {
                    "success": True, "message": "data fetched succeessfully", "data": data}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in Messages"}
                return(response)
        except Exception as e:
            return({"success": False, "error_message": "server is down try after sometime", "error": str(e)})

    # post Groups
    def post(self):
        try:
            request_json_object = request.get_json()
            schema = AddMessageschema()
            new_Group_obj = schema.load(
                request_json_object, session=db.session).data
            db.session.add(new_Group_obj)
            db.session.commit()
            data = schema.dump(new_Group_obj).data
            Group_response = {
                "success": True, "message": "Message registered succeessfully", "data": data}
            return (Group_response)
        except Exception as e:
            return({"success": False, "message": str(e.args)})









class GetGroupMessages(Resource):
    def __init__(self):
        pass

    # Groups get call based on id
    def get(self, id):
        try:
            Group = Messages.query.filter(Messages.groupId == id).all()
            if len(Group)>0:
                Group_schema = MessagesSchema(many=True)
                data = Group_schema.dump(Group).data
                Group_response = {"success": True, "message":"data fetched successfully", "data": data}
                return (Group_response)
            else:
                response = {"success": False, "message": "no data found on this id", "id": id}
                return(response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e)})


class UpdatemessageLikes(Resource):
    def __init__(self):
        pass
    # get all Groups

    def put(self,id):
        try:
            likes = request.get_json()
            obj = Messages.query.filter(Messages.id == id).one_or_none()
            if obj is not None:
                schema = MessagesSchema()
                data = schema.dump(obj).data
                if data['userLikes'] is None:
                
                    userlikes = [likes['userLikes']]
                elif likes['userLikes'] in data['userLikes']:
                    return {"success": True, "message": "Already Liked Message"}
                else:
                    userlikes = data['userLikes']
                    userlikes.append(likes['userLikes']) 
                Messages.query.filter(Messages.id == id).update({"userLikes":userlikes})
                db.session.commit()
                obj = Messages.query.filter(Messages.id == id).first()
                schema = MessagesSchema()
                data = schema.dump(obj).data
                response = {
                    "success": True, "message": "data fetched succeessfully", "data": data}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in GroupMembers"}
                return(response)
        except Exception as e:
            return({"success": False, "error_message": "server is down try after sometime", "error": str(e)})

    
