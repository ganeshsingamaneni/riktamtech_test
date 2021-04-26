from flask import Flask
from flask_restful import Api
import os
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager

# ma = Marshmallow(app) 

workdir = os.getcwd()



app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)



app.config["SQLALCHEMY_ECHO"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@localhost:3306/riktam"


app.config['SECRET_KEY'] = '3b8d7b303173189153979542'

# app.config['JWT_SECRET_KEY'] = 'JwtAuthToken'

# app.config['JWT_BLACKLIST_ENABLED'] = True

# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

# jwt = JWTManager(app)

ma = Marshmallow(app)

db.init_app(app)
