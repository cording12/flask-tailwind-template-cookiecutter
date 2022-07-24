"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment

from .assets import compile_assets

assets = Environment()


def create_app():
    """ Create Flask application """
    app = Flask(__name__, instance_relative_config=False)
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object('config.DevelopmentConfig')

    # Initialize plugins
    assets.init_app(app)

    with app.app_context():
        from .home import routes as home

        app.register_blueprint(home.home_bp)

        compile_assets(assets)

        return app
