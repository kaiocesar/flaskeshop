# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.jsontools import JsonSerializableBase
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(cls=(JsonSerializableBase,))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/flaskeshop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Product(db.Model, Base):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45))
	description = db.Column(db.Text)
	amount = db.Column(db.Integer)
	price = db.Column(db.Float(precision=2))
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)

	def __init__(self, name, description, amount, price, created_at, updated_at):
		self.name = name
		self.description = description
		self.amount = amount
		self.price = price
		self.created_at = created_at
		self.updated_at = updated_at

	def __repr__(self):
		return '<Product %r>' % self.name

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

