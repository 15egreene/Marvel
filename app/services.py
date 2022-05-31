from app.models import User, Post, db

def userinfo(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(author=user.id).all()
    for p in posts:
        p.timestamp = str(p.timestamp)[:-7]
