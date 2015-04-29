# -*- coding:utf-8 -*-

from app import db


class Datasets(db.Model):
	"""docstring for Cshort_namelassName"""
	id = db.Column(db.INTEGER, primary_key = True)
	short_name = db.Column(db.VARCHAR(64), index = True, unique = False)
	long_name = db.Column(db.VARCHAR(255),  unique = False)
	website = db.Column(db.VARCHAR(255), index = True, unique = False)
	category = db.Column(db.VARCHAR(64), index = True, unique = False)
	flag = db.Column(db.INTEGER, unique = False)

	def __repr__(self):
		return '<Datasets %r>' % (self.short_name)