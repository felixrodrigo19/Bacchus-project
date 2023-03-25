from flask_admin import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required, SimpleLogin

from bacchus.ext.login.auth_service import AuthService

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


def init_app(app):
    auth_service = AuthService()
    SimpleLogin(app, auth_service.verify_login)
