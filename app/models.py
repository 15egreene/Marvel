

from secrets import token_hex

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from flask_login import LoginManager, UserMixin

login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)


from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.String(40), primary_key= True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email =  db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255), default='No bio.')
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(100))
    posts = db.relationship('Post', backref='post_author')

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)
        self.api_token = token_hex(16)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())    
    author = db.Column(db.String, db.ForeignKey('user.id'))


class MarvelHero(db.Model):

    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    abilities = db.Column(db.String(255))
    alias = db.Column(db.String(255))
    height = db.Column(db.Unicode, default=None)
    weight = db.Column(db.Unicode, default=None)
    gender = db.Column(db.String)
    image = db.Column(db.String(255))
    bio = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())


    def __init__(self, dict):
        self.id = str(uuid4())
        self.name = dict.get('name').title()
        self.bio = dict.get('bio')
        self.abilities = dict.get('abilities', 'unknown')
        self.alias = dict.get('alias')
        self.image = dict.get('image')
        self.gender = dict.get('gender', 'unknown')


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'abilities': self.abilities,
            'bio': self.bio,
            'alias': self.alias,
            'gender': self.gender
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])


