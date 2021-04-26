import datetime
from config import db
from sqlalchemy.orm import validates
from usersmicroservice.models.users import Users
from groupsmicroservice.models.groups import Groups

class Messages(db.Model):
    __tablename__ = "messages"

    """
    Represents  Users

    field id: Primary key
    type id: Integer

    field message
    type :Text
    
    field groupId
    type: integer
    
    field userId
    type: Integer

    field userLikes
    type: Text

    field createdAt
    type: Datetime
    
    field updatedAt
    type: Datetime

    """
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text,nullable=False)
    groupId = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    userLikes = db.Column(db.JSON,nullable = True)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatedAt = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

   
  
