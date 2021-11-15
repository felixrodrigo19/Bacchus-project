from dynaconf import FlaskDynaconf


def init_app(app):
    app.config.update(
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
    )
    FlaskDynaconf(app)
