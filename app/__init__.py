from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.secret_key = 'some_very_strong_secret_key'
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/testdb'
db = SQLAlchemy(application)
migrate = Migrate(application, db)

application.app_context().push()

from app.auth.views import auth as blueprint_auth
from app.friends.views import friend as blueprint_friend
from app.profile.views import profile as blueprint_profile

application.register_blueprint(blueprint_auth)
application.register_blueprint(blueprint_profile)
application.register_blueprint(blueprint_friend)
