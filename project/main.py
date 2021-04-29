# main.py

from flask import Blueprint, render_template,request
from flask_restplus import Resource, Api
from marshmallow import Schema, fields
from .models import Games
from . import db
from flask_jwt_extended import jwt_required
class GameSchema(Schema):
	id = fields.Int()
	title = fields.Str()
	platform = fields.Str()
	score = fields.Int()
	genre = fields.Str()
	editors_choices = fields.Bool()
gameSchema=GameSchema(many=True)
class GamesApi(Resource):
	@jwt_required
	def get(self):
		games=Games.query.all()
		print(games)
		rt=gameSchema.dumps(games)
		return rt,201
	@jwt_required
	def post(self):
		body=request.get_json()
		game = Games()
		for key,value in body.items():
			setattr(game,key,value)
		id=game.title
		db.session.add(game)
		db.session.commit()
		return {"title": id} , 200
	@jwt_required
	def delete(self, id):
		game=Games.query.filter_by(id=id).first()
		db.session.delete(game)
		db.session.commit()
		return {"id": id}, 204
	@jwt_required
	def put(self,id):
		game= Games.query.filter_by(id=id).first()
		body=request.get_json()
		for key,value in body.items():
			if key is not None:
				setattr(game, key, value)
		db.session.commit()
		return {"id": id} ,203
class GamesApiS(Resource):
	@jwt_required
	def get(self,title):
		print(title)
		game= Games.query.filter_by(title=title).all()
		if not game:
			return {"Resource":"game not found"},404
		return gameSchema.dump(game),200











