#!/usr/bin/env python3
import re
import os
from datetime import datetime
import logging

import flask
from flask import (
    Flask, 
    request, 
    jsonify, 
    render_template
) 
import sqlalchemy.exc as sqlexc
from email_validator import validate_email, EmailNotValidError

import database
from database import db

# Init app 
app = Flask(__name__)

# Init the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def main_page():
    members = database.Member.query.all()
    return render_template('main.htm', members=members)

@app.route('/', methods=['POST'])
def add_member():
    try:
        name = request.form['name']
        reg = r'[A-Za-z.\s]+'
        if not re.fullmatch(reg, name):
            raise ValueError('Incorrect name format')
        re.fullmatch(reg, name)
        email = request.form['email']
        validate_email(email)
    except (KeyError, ValueError, EmailNotValidError) as e:
        members = database.Member.query.all()
        return render_template('main.htm', members=members, formerror=str(e))
        
    registration_date = datetime.now()
    print(registration_date)

    try:
        member = database.Member(name, email, registration_date)
        db.session.add(member)
        db.session.commit()
        logging.info(f'added member {email} successfully')
    except sqlexc.IntegrityError as e:
        db.session.rollback()
        members = database.Member.query.all()
        formerror = f'A member with email {email} already exists'
        return render_template('main.htm', members=members, formerror=formerror)
    return flask.redirect(flask.url_for('main_page'))

if __name__ == '__main__':
    debug = 'DEBUG' in os.environ
    port = int(os.environ.get('PORT', 5000))
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    db.init_app(app)
    db.create_all(app=app)
    app.run(host='0.0.0.0', port=port, debug=debug)