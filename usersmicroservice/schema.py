from marshmallow import fields,Schema
from config import ma, db
from usersmicroservice.models.users import Users
from marshmallow_sqlalchemy import ModelSchema


class UsersSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ('id','userName', 'email')
        sqla_session = db.session

class AddUserSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ('id', 'userName', 'email', 'status', 'password')
        sqla_session = db.session

class SigninSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ('id','userName','email')
        sqla_session = db.session

class GetUsersSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ('id','userName', 'email')
        sqla_session = db.session