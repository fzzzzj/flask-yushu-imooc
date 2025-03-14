"""
 Created by 七月 on 2018-3-12.
"""
from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import EqualTo, Length, NumberRange, DataRequired, Email, \
    ValidationError

from app.models.user import User

__author__ = '七月'


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    @staticmethod
    def validate_email(field):
        # db.session.
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    @staticmethod
    def validate_nickname(field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])


class ChangePasswordForm(Form):
    old_password = PasswordField(validators=[DataRequired()])
    new_password1 = PasswordField(validators=[
        DataRequired(), Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('new_password2', message='两次输入的密码不一致')])
    new_password2 = PasswordField(validators=[DataRequired()])
