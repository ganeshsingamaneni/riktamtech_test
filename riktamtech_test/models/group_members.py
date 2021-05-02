import datetime
from config import db
from sqlalchemy.orm import validates
from models.users import Users
from models.groups import Groups

class GroupMembers(db.Model):
    __tablename__ = "groupmembers"

    """
    Represents  Users

    field id: Primary key
    type id: Integer

    field groupId
    type :Integer
    
    field userID
    type: integer
    
    field isAdmin
    type: boolean

    field createdAt
    type: Datetime
    
    field updatedAt
    type: Datetime

    """
    id = db.Column(db.Integer, primary_key=True)
    groupId = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatedAt = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

   
  
