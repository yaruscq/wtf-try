import os
from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .wtf_forms import loginForm
from .models import get_user_by_username, User, users

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
	form = loginForm()
	if form.validate_on_submit():

		user_object = next((user for user in users.values() if user.username == form.username.data), None)

		login_user(user_object)
		# if current_user.is_authenticated:
		# 	flash("登入成功！", 'success')
		# 	return redirect(url_for('main.chat'))
		return redirect(url_for('main.chat'))
	# else:
	# 	return redirect(url_for(main.index))
	return render_template('index.html', form=form, msg="歡迎前來與我一敘！")



@main.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():

	# if not current_user.is_authenticated:
	# 	return "請先登入，再使用 Chat!"
	
	msg = "You're in the chatroom!"

	# response = make_response(render_template('chat.html', msg=msg))
	
	# # Set Cache-Control headers
	# response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"

	# response.headers["Pragma"] = "no-cache"  # for HTTP 1.0 compatibility

	# return response
	return render_template('chat.html', msg=msg)


@main.route('/logout', methods=['GET'])
# @login_required
def logout():
	
	if current_user.is_authenticated:
		username = current_user.username.capitalize()
		logout_user()
		flash(f'{username}, 你已經被登出！', 'info')
		return redirect(url_for('main.index'))
	return redirect(url_for('main.index'))