import dash
import dash_bootstrap_components as dbc
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required

from config import BaseConfig


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashapps(server)
    register_extensions(server)
    register_blueprints(server)

    return server


def register_dashapps(app):
    from app.dashbelly.layout import layout
    from app.dashbelly.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    dashbelly = dash.Dash(
        __name__,
        server=app,
        url_base_pathname="/dashboard/",
        assets_folder=get_root_path(__name__) + "/dashboard/assets/",
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        meta_tags=[meta_viewport],
    )

    with app.app_context():
        dashbelly.title = "Dash Belly"
        dashbelly.layout = layout
        register_callbacks(dashbelly)


####
#### Disabled for dev purposes.
####

#     _protect_dashviews(dashbelly)


# def _protect_dashviews(dashapp):
#     for view_func in dashapp.server.view_functions:
#         if view_func.startswith(dashapp.config.url_base_pathname):
#             dashapp.server.view_functions[view_func] = login_required(
#                 dashapp.server.view_functions[view_func]
#             )


def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(server)
    login.init_app(server)
    login.login_view = "main.login"
    migrate.init_app(server, db)


def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp)
