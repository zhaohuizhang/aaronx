# -*- coding:utf-8 -*-

from app import db,app
from flask import render_template, flash, redirect, session, url_for, request, g
from models import Datasets


@app.route('/',methods=['GET','POST'])
def show_entries():
	datasets = Datasets.query.all()
	return render_template('show_entries.html', results = datasets)

@app.route('/add',methods=['POST'])	
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	post = Datasets(short_name = request.form['short_name'], long_name = request.form['long_name'], website = request.form['website'], category = request.form['category'])
	db.session.add(post)
	db.session.commit()
	flash('New datasource was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('Welcome our web site!')
			return redirect(url_for('show_entries'))
	return	render_template('login.html', error = error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))
