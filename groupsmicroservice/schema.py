from marshmallow import fields,Schema
from config import ma, db
from groupsmicroservice.models.groups import *
from marshmallow_sqlalchemy import ModelSchema
from groupsmicroservice.models.group_members import *


class GroupsSchema(ma.ModelSchema):
    class Meta:
        model = Groups
        fields = ('id','name','createdBy')
        sqla_session = db.session

class AddGroupschema(ma.ModelSchema):
    class Meta:
        model = Groups
        fields = ('id', 'name', 'createdBy')
        sqla_session = db.session


class GetgroupsSchema(ma.ModelSchema):
    class Meta:
        model = Groups
        fields = ('id','name', 'createdBy')
        sqla_session = db.session

class AddGroupMemberschema(ma.ModelSchema):
    class Meta:
        model = GroupMembers
        fields = ('id','userId', 'groupId','isAdmin')
        sqla_session = db.session
