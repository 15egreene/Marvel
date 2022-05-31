from app import app

from app.models import db, MarvelHero, User, Post

@app.shell_context_processor
def shell_context():
    return {'db': db, 'MarvelHero': MarvelHero, 'User': User, 'Post': Post}