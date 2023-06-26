from flask import Blueprint, jsonify, request

from app.auth.models import User

friend = Blueprint('blueprint_friend', __name__)


@friend.route('/print', methods=["POST"])
# @login_required
def print_text():
    """ Список друзей пользователя """
    data = request.get_json()
    user = User.query.filter_by(id=data.get('id')).first()
    friends_dict = [obj.serialize() for obj in user.friends]

    return jsonify(friends_dict)

