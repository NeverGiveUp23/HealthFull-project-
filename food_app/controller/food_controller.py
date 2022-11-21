from flask import render_template, session, redirect, request, flash, jsonify
import re
import requests
from flask_bcrypt import Bcrypt
from food_app import app
import os
from food_app.model.login_model import User
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/searching", methods=['POST'])
def search():

    # r = requests.get(f" https://api.edamam.com/auto-complete?app_id=0e94fdc3&app_key=7624707be5246cd1f379234f5c40c602&q=steak/")
    return jsonify(r.json())


#  ======== Login Section with validation ======


@app.route('/login/register')
def reg():
    return render_template('login.html')


@app.route("/register", methods=['POST'])
def reg_user():
    valid = User.validate_user(request.form)

    if not valid:
        return redirect('/login/register')

    new_user = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }

    user_id = User.save(new_user)
    if not user_id:
        flash("Email already taken.", "register")
        return redirect('/login/register')

    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    return redirect('/login/register')


@app.route("/login", methods=['POST'])
def login_user():

    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password", "login")
        return redirect("/login/register")
    #  this is checking the valid password if it matches anything in the database
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect("/login/register")
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
