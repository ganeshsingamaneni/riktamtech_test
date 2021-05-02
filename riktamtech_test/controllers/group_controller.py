import datetime
import os
# import yaml
from flask import request
from flask_restful import Api, Resource
from sqlalchemy import exc
import sqlalchemy.exc as sqlalchemy_exc
from config import db
from models.groups import Groups
from schemas.groupschema import *

from sqlalchemy import or_,and_





class GetAddGroups(Resource):
    def __init__(self):
        pass
    # get all Groups

    def get(self):
        try:
            Group_id = request.headers.get('group_id')
            obj = Groups.query.filter(Groups.id != Group_id).order_by(Groups.id).all()
            if obj:
                schema = GroupsSchema(many=True)
                data = schema.dump(obj).data
                response = {
                    "success": True, "message": "data fetched succeessfully", "data": data}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in Groups"}
                return(response)
        except Exception as e:
            return({"success": False, "error_message": "server is down try after sometime", "error": str(e)})

    # post Groups
    def post(self):
        try:
            request_json_object = request.get_json()
            schema = AddGroupschema()
            new_Group_obj = schema.load(
                request_json_object, session=db.session).data
            db.session.add(new_Group_obj)
            db.session.commit()
            data = schema.dump(new_Group_obj).data
            memschema = AddGroupMemberschema()
            membdata = {"groupId":data['id'],"userId":request_json_object['createdBy'],"isAdmin":1}
            new_GroupMem_obj = memschema.load(
                membdata, session=db.session).data
            db.session.add(new_GroupMem_obj)
            db.session.commit()
            # data = schema.dump(new_Group_obj).data
            Group_response = {
                "success": True, "message": "Group registered succeessfully", "data": data}
            return (Group_response)
        except Exception as e:
            return({"success": False, "message": str(e.args)})









class GetGroup(Resource):
    def __init__(self):
        pass

    # Groups get call based on id
    def get(self, id):
        try:
            Group = Groups.query.filter(Groups.id == id).one_or_none()
            if Group is not None:
                Group_schema = GroupsSchema()
                data = Group_schema.dump(Group).data
                Group_response = {"success": True, "message":"data fetched successfully", "data": data}
                return (Group_response)
            else:
                response = {"success": False, "message": "no data found on this id", "id": id}
                return(response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e)})


class GetGroupMembers(Resource):
    def __init__(self):
        pass
    # get all Groups

    def get(self,id):
        try:
            obj = GroupMembers.query.filter(GroupMembers.groupId == id).order_by(GroupMembers.id).all()
            if obj:
                schema = AddGroupMemberschema(many=True)
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

    
class AddGroupMembers(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            request_json_object = request.get_json()
            groupmemexist = db.session.query(GroupMembers).filter(and_(GroupMembers.userId == request_json_object['userId'],GroupMembers.groupId==request_json_object['groupId'])).one_or_none()
            print(groupmemexist)
            if groupmemexist is None:
                memschema = AddGroupMemberschema()
                new_GroupMem_obj = memschema.load(
                    request_json_object, session=db.session).data
                db.session.add(new_GroupMem_obj)
                db.session.commit()
                data = memschema.dump(new_GroupMem_obj).data
                Group_response = {
                    "success": True, "message": "Group Member registered succeessfully", "data": data}
                return (Group_response)
            return {"success": False, "message": "Group Member already exists"}    
        except Exception as e:
            return({"success": False, "message": str(e.args)})    

class DeleteGroupMembers(Resource):
    def __init__(self):
        pass
    # get all Groups

    def delete(self):
        try:
            # Roles.query.filter(Roles.id == 1).one_or_none()
            user = request.args.get('user')
            group = request.args.get('group')
            obj = GroupMembers.query.filter(and_(GroupMembers.userId == user,GroupMembers.groupId==group)).one_or_none()
            if obj is not None:
                GroupMembers.query.filter(GroupMembers.id == obj.id).delete()
                db.session.commit()
                response = {
                    "success": True, "message": "Member removed"}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in GroupMembers"}
                return(response)
        except Exception as e:
            return({"success": False, "error_message": "server is down try after sometime", "error": str(e)})            