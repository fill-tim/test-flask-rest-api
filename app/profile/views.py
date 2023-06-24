from flask import Blueprint, jsonify
from app.auth.models import User

profile = Blueprint('profile', __name__)


@profile.route('/profile/<username>', methods=["GET"])
def profile_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return {'message': 'Пользователь не существует!'}
    return jsonify(user.serialize())
