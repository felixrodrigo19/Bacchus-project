from flask_admin import Admin
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, filters
from bacchus.ext.db import db
from bacchus.ext.db.models import User

from flask import flash


page_admin = Admin()


class AdminView(ModelView):
    can_view_details = True
    column_exclude_list = ['passwd', 'updated_on']
    column_searchable_list = ["email"]
    form_excluded_columns = ["updated_on", "created_on"]
    column_filters = [
        "email",
        "admin"
    ]

    can_edit = False
    can_create = True
    can_delete = True

    

def init_app(app):
    page_admin.init_app(app)
    page_admin.name = app.config["ADMIN_NAME"]
    page_admin.template_mode='bootstrap3'
    page_admin.add_view(AdminView(User, db.session))
