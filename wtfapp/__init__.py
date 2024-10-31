from flask import Flask
from .routes import main
from flask_login import LoginManager, login_user, current_user
from .config import Config
from .models import User, users

# login_manager = LoginManager()

# @login_manager.user_loader
# def load_user(user_id):
# 	return users.get(str(user_id))

def create_app():

	app = Flask(__name__)
	app.config.from_object(Config)

	# login_manager.init_app(app)
	# login_manager.login_view = 'main.index'

	# app.config['SECRET_KEY'] = 'secret'
	from .routes import main
	app.register_blueprint(main)

	return app