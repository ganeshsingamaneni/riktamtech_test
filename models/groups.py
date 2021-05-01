import datetime
from config import db
from sqlalchemy.orm import validates
from models.users import Users


class Groups(db.Model):
    __tablename__ = "groups"

    """
    Represents  Users

    field id: Primary key
    type id: Integer

    field name
    type :string
    
    field status
    type: boolean
    
    field createdBy
    type: UserId

    field createdAt
    type: Datetime
    
    field updatedAt
    type: Datetime

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(220), nullable=False)
    createdBy = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatedAt = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

   
  
