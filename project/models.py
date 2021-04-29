# models.py

from flask_login import UserMixin
from . import db
from flask_bcrypt import generate_password_hash, check_password_hash
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    def check_password(self, password):
    	self.password = check_password_hash(password,self.password).decode('utf8')
    def hash_password(self):
    	self.password = generate_password_hash(self.password).decode('utf8')
class Games(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	platform = db.Column(db.String(100))
	score = db.Column(db.Integer)
	genre = db.Column(db.String(100))
	editors_choices = db.Column(db.Boolean)