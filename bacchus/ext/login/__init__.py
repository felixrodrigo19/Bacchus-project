from flask_simplelogin import SimpleLogin, login_required
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask import request
from bacchus.ext.db.models import User


def verify_login(user):
    db_result = User.query.filter_by(email=user.get("username")).first()
    if db_result is not None:
        if (user.get("username") == db_result.email and
            user.get("password") == db_result.passwd):
            return True
        else:
            return False
    else:
        return False


AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
