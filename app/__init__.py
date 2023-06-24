from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.secret_key = 'some_very_strong_secret_key'
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/testdb'
db = SQLAlchemy(application)

application.app_context().push()

from app.auth.views import auth as blueprint_auth
from app.friends.views import friend as blueprint_friend

application.register_blueprint(blueprint_auth)
application.register_blueprint(blueprint_friend)
