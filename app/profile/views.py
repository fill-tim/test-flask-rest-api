from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from app import db
from app.auth.models import User

profile = Blueprint('blueprint_profile', __name__)


@profile.route('/profile/<username>', methods=["GET"])
def profile_user(username):
    """ Профиль пользователя """
    user = User.query.filter_by(username=username).first()
    if not user:
        return {'message': 'Пользователь не существует!'}
    return jsonify(user.serialize())


@profile.route('/update', methods=["POST"])
@login_required
def update_profile():
    """ Изменить данные профиля пользователя """
    data = request.get_json()
    if data != {}:
        user_id = current_user.get_id()
        data['password'] = generate_password_hash(data['password'])
        try:
            user = User.query.filter_by(id=user_id)
            user.update(data)
            db.session.commit()
            return {"message": "Данные были изменены!"}
        except:
            return {"message": "Данные не были изменены"}
    return {"message": "Данные не были введены!"}
