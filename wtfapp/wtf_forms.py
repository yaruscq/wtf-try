# from collections.abc import Sequence
# from typing import Any, Mapping
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from .models import User, users, get_user_by_username, get_user_by_email

class loginForm(FlaskForm):
    username = StringField('會員名字：', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder" : "請輸入名字..."})
    email = StringField('電子信箱：', validators=[DataRequired()], render_kw={"placeholder" : "請輸入電子信箱..."})
    
    submit = SubmitField('登 入')
    
    def validate_username(self, username):
        # if not super().validate():
        #    return False
        user_object = get_user_by_username(self.username.data)
        # if user_object is None:
        if user_object is None:
           raise ValidationError("你不是會員！")

        
    def validate_email(self, email):
        # if not super().validate():
        #    return False
        user_object = get_user_by_email(self.email.data)
        if user_object is None:
           raise ValidationError("你的電子信箱錯誤！")
        if user_object.username != self.username.data:
           raise ValidationError("電子信箱和使用者不符合！")

        
    # def validate_login(self):
    #     if not super().validate():
    #        return False
    #     user_object = get_user_by_username(self.username.data)
		
    #     if user_object is None:
    #        self.username.errors.append('不是會員！')
    #        return False

    #     if user_object.email != self.email.data:
    #        self.email.errors.append('電子信箱和使用者不合！')
    #        return False

    #     return True
