import datetime
from config import db
from sqlalchemy.orm import validates



class Users(db.Model):
    __tablename__ = "users"

    """
    Represents  Users

    field id: Primary key
    type id: Integer

    field email
    type : string

    field userName
    type :string
    
    field password
    type: string

    field status
    type: boolean

    field createdAt
    type: Datetime
    
    field updatedAt
    type: Datetime

    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(220), nullable=False)
    userName = db.Column(db.String(220), nullable=False)
    password = db.Column(db.String(220), nullable=False)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatedAt = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

   
    @validates('businessEmail')
    def validate_email(self, key, address):
        assert '@' in address
        return address
