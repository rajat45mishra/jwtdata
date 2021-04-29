from flask_restplus import Resource
from flask_jwt_extended import create_access_token
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import timedelta
from .models import User
from flask import request
from . import db
class SignupApi(Resource):
 def post(self):
   body = request.get_json()
   print(body)
   user = User()
   for key,value in body.items():
    if key is not None:
        setattr(user,key,value)
   user.hash_password()
   db.session.add(user)
   db.session.commit()
   id = user.id
   return {'id': str(id)}, 200


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.query.filter_by(email=body.get('email')).first()
        authorized = check_password_hash(user.password,body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        expires = timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
