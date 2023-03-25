from bacchus.ext.site.main import site_bp


def init_app(app):
    app.register_blueprint(site_bp)
