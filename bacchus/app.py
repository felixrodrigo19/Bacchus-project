from flask import Flask

from bacchus.ext import site
from bacchus.ext import db
from bacchus.ext import migrate
from bacchus.ext import admin
from bacchus.ext import cli
from bacchus.ext import config
from bacchus.ext import login


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    admin.init_app(app)
    cli.init_app(app)
    site.init_app(app)

    return app
