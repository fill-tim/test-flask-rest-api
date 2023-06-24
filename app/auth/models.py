from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

from app.friends.models import friendship
from app.friends.serializers import FriendListSerializer


class User(db.Model, FriendListSerializer, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    friends = db.relationship("User", secondary=friendship, primaryjoin=id == friendship.c.user_id,
                              secondaryjoin=id == friendship.c.friend_id)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "friends": self.friend_serialize(self.friends)
        }
