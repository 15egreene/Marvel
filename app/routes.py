import requests as r 
from app import app
from .models import User, Post, db
from flask import render_template, redirect
from flask_login import current_user, login_required
from .services import userinfo


@app.route('/')
def home():
    greeting = 'Hello, Enrique'
    print(greeting)
    return render_template('index.html', g=greeting)





@app.route('/characters')
@login_required
def characters():
    return render_template('index3.html')

@app.route('/services')
def movies():
    return render_template('services.html')


@app.route('/games')
def games():
    return render_template('index6.html')


@app.route('/videos')
def videos():
    return render_template('index2.html')

@app.route('/comics')
def comics():
    return render_template('index4.html')


@app.route('/blog', methods=['GET','POST'])
@login_required
def userinfo(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(author=user.id).all()
    for p in posts:
        p.timestamp = str(p.timestamp)[:-7]

    return render_template(user=user, posts=posts)
