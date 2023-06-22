from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask_login import login_user, LoginManager, logout_user, login_required, current_user

auth = Blueprint('blueprint_auth', __name__)

from app.auth.models import User, db

login_manager = LoginManager()

from app import application

login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth.route('/register', methods=["POST"])
def register_user():
    """ Регистрация пользователя """
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()

    if user:
        return {'message': "Пользователь уже существует!"}
    else:
        try:
            db.session.add(User(**data))
            db.session.commit()
            return {"message": 'Пользователь зарегистрирован!', "status": 201}
        except Exception as e:
            raise {'message': str(e), 'status': 404}


class LoginUser(MethodView):
    """ Авторизация пользователя """
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data.get('email')).first()
        check = self.valid_login(data, user)
        return check

    def valid_login(self, post_data, user_obj):
        email = post_data.get('email')
        password = post_data.get('password')

        if not user_obj:
            return {'message': 'Пользователь не существует!', 'status': 404}

        if user_obj.email == email and user_obj.check_password(password):
            return self.login(user_obj)
        else:
            return {'message': 'Логин или пароль введены неправильно!', 'status': 404}

    def login(self, obj):
        login_user(obj)
        return {'message': 'Пользователь авторизован!', 'status': 200}


auth.add_url_rule('/login', view_func=LoginUser.as_view('user_auth'), methods=['POST'])


@auth.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    """ Разлогиниться """
    logout_user()
    return {'message': 'Пользователь вышел!'}


@auth.route('/user', methods=["GET"])
@login_required
def check_user():
    """ Получаем текущего пользователя из current_user """
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }


@auth.route('/print', methods=["GET"])
@login_required
def print_text():
    """ Список всех пользователей """
    users_list = User.query.all()
    users_dict = [user.serialize() for user in users_list]

    return jsonify(users_dict)
