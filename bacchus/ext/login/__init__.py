from flask_admin import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required, SimpleLogin

from bacchus.ext.login.auth_service import AuthService


class AdminService:
    @staticmethod
    @login_required
    def admin_index():
        return AdminIndexView._handle_view

    @staticmethod
    @login_required
    def model_view():
        return sqla.ModelView._handle_view


def init_app(app):
    admin_service = AdminService()
    auth_service = AuthService()
    SimpleLogin(app, auth_service.verify_login)
    AdminIndexView._handle_view = admin_service.admin_index
    sqla.ModelView._handle_view = admin_service.model_view
