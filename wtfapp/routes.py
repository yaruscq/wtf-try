import os
from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .wtf_forms import loginForm
from .models import get_user_by_username, User

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
	form = loginForm()
	if form.validate_on_submit():
		# flash(f"{user_object.username}, 登入成功！", 'success')
		flash("登入成功！", 'success')
		return redirect(url_for('main.chat'))
	# else:
	# 	return redirect(url_for(main.index))
	return render_template('index.html', form=form, msg="歡迎前來與我一敘！")
	
	# if current_user.is_authenticated:
	# 	return redirect(url_for('main.chat'))

	# form = loginForm()
	# name1 = os.getenv('name1')
	# name2 = os.getenv('name2')

	# if form.validate_on_submit():
		
	# 	user_object = get_user_by_username(form.username.data)
	# 	username = form.username.data
	# 	if user_object is not None:
	# 		# login_user(username)
	# 		flash(f"{user_object.username}, 登入成功！", 'success')
	# 		return redirect(url_for('main.chat'))
		
	# 	else:
	# 		flash(f'"{username}" 你不是會員！請輸入會員大名。', 'error')
	# 		# return redirect(url_for('main.index'))
	# 		return redirect('/')

        # return render_template('index.html', form=form, msg="歡迎前來與我一敘！")



@main.route('/chat')
# @login_required
def chat():
	msg = "You're in the chatroom!"
	return render_template('chat.html', user=current_user, msg=msg)


@main.route('/logout')
# @login_required
def logout():
# 	logout_user()
# 	flash('你已經被登出！', 'info')
	return redirect(url_for('main.index'))