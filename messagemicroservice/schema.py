from marshmallow import fields,Schema
from config import ma, db
from marshmallow_sqlalchemy import ModelSchema
from messagemicroservice.models.messages import Messages


class MessagesSchema(ma.ModelSchema):
    class Meta:
        model = Messages
        fields = ('id','message','groupId','userId','userLikes')
        sqla_session = db.session

class AddMessageschema(ma.ModelSchema):
    class Meta:
        model = Messages
        fields = ('id','message','groupId','userId')
        sqla_session = db.session


# class MessagesSchema(ma.ModelSchema):
#     class Meta:
#         model = Messages
#         fields = ('id','name', 'createdBy')
#         sqla_session = db.session

# class AddGroupMemberschema(ma.ModelSchema):
#     class Meta:
#         model = GroupMembers
#         fields = ('id','userId', 'groupId','isAdmin')
#         sqla_session = db.session
