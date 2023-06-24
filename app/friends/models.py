from app import db

friendship = db.Table(
    'friendship',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('friend_id', db.Integer(), db.ForeignKey('user.id'))
)
