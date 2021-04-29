# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
from .auth import SignupApi,LoginApi
from .main import GamesApi,GamesApiS
api = Api()
bcrypt = Bcrypt()
JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
jwt = JWTManager()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{username}:{password}@{server}/testdb".format(username, password, server)
    db.init_app(app)
    api.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    # blueprint for auth routes in our app
    return app


api.add_resource(SignupApi,"/api/Signup")
api.add_resource(LoginApi,"/api/LoginApi")
api.add_resource(GamesApi,"/api/AllGames")
api.add_resource(GamesApi,"/api/AllGames/<int:id>")
api.add_resource(GamesApiS,"/api/search/<title>")
