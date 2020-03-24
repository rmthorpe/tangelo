#!/usr/bin/env python

#-----------------------------------------------------------------------
# routes.py
#-----------------------------------------------------------------------

from tangelo import app, db
from tangelo.CASClient import CASClient
from tangelo.tangeloService import getGreetingDayTime
from tangelo.models import User
from flask import request, make_response, abort, redirect, url_for
from flask import render_template, session
from flask_login import login_user, logout_user, login_required #, current_user
from tangelo.generic import generic
 
#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():
    html = render_template('index.html',
        ampm=getGreetingDayTime())
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/login', methods=['GET'])
def login():

    username = CASClient().authenticate()

    user = User.query.filter_by(netid=username).first()
    login_user(user)
    # redirect to requested page
    next_page = request.args.get('next')
    return redirect(next_page) if next_page else redirect(url_for('index'))

#-----------------------------------------------------------------------

@app.route('/logout')
def logout():

    casClient = CASClient()
    casClient.authenticate()
    logout_user()
    casClient.logout()

#-----------------------------------------------------------------------

@app.route('/about', methods=['GET'])
def about():

    html = render_template('about.html',
        ampm=getGreetingDayTime())
    response = make_response(html)
    return response

#----------------------------------------------------------------------
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    html = render_template('account.html')
    response = make_response(html)
    return response

#----------------------------------------------------------------------
@app.route('/generic')
@login_required
def genericSetup():
    html = render_template('generic.html')
    response = make_response(html)
    return response

