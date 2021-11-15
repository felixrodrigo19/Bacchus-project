from flask_migrate import Migrate
from bacchus.ext.db import db
from bacchus.ext.db import models # NOQA


migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
