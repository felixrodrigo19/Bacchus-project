import click
from bacchus.ext.db import db
from bacchus.ext.db import models


def init_app(app):
    @app.cli.command()
    def create_db():
        """ Inicia o banco """
        db.create_all()
        click.echo("DB criado com sucesso!")


    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """ Adiciona usuario """
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()


    @app.cli.command()
    @click.option("--email", "-e")
    def delete_user(email):
        """ Deleta usuario """
        user = models.User(
            email=email
        )
        db.session.delete(user)
        db.session.commit()


    @app.cli.command()
    def list_users():
        """ Lista todos usuarios """
        user = models.User.query.all()
        click.echo(f"{user}")
