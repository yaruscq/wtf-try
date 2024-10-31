#wtfapp/__init__.py

from flask import Flask, make_response
from .routes import main
from flask_login import LoginManager, login_user, current_user, set_login_view
from .config import Config

from .events import *
from . import socketio
# models 不可在 .events 和 socketio 之前
from .models import User, users, get_user_by_username



login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
	print('\n\nuser_id = ' + user_id + '\n\n')
	return next((user for user in users.values() if user.id == user_id), None)
	# return users.get(str(user_id))





def create_app():

	app = Flask(__name__)
	app.config.from_object(Config)

	login_manager.init_app(app)
	login_manager.login_view = 'main.index'
	login_manager.login_message = "先登入，才能進去聊天室！"

	socketio.init_app(app)

	# app.config['SECRET_KEY'] = 'secret'
	from .routes import main
	app.register_blueprint(main)

	@app.after_request
	def app_caching(response):
		response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, public, max-age=0"
		return response

    # Globally defined 沒有用！
	# @app.before_request
	# def add_cache_control_headers():
	# 	response = make_response()
	# 	response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
	# 	response.headers['Pragma'] = 'no-cache'
	

	return app