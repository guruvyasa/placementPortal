from flask import Flask, render_template, redirect,request,url_for
from placementPortal import app
from .database import db_session
from .database import create_user

@app.route('/signup', methods=['POST','GET'])
def user_register():
    # complaint_types =
    if request.method == 'POST':
        redirect(url_for('register_user'))
    elif request.method == 'GET':
        return render_template('userRegister.html')

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register_user', methods=['POST'])
def register_user():
    name = request.form['name']
    username = request.form['username']
    usn = request.form['usn']
    email = request.form['email']
    password = request.form['password']
    create_user(usn, name, username, email, password)
    return redirect(url_for('login'))






