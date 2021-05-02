from flask import Flask
from flask_restful import Api
import os
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# from flask_socketio import SocketIO


# ma = Marshmallow(app) 

workdir = os.getcwd()



app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# socketio = SocketIO(app, cors_allowed_origins="*")


db = SQLAlchemy(app)



app.config["SQLALCHEMY_ECHO"] = False

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@localhost:3306/riktam"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////"+workdir+"/development.db"

app.config['SECRET_KEY'] = '3b8d7b303173189153979542'



ma = Marshmallow(app)

db.init_app(app)
