from bacchus.ext.db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    passwd = db.Column("passwd", db.Unicode, nullable=False)
    admin = db.Column("admin", db.Boolean)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                            server_onupdate=db.func.now())

    def __repr__(self):
        return self.email


    @property
    def is_authenticated(self):
        return True