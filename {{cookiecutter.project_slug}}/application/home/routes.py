""" This is the home route """
# Import flask components
from flask import Blueprint
from flask import current_app as app
from flask import redirect, render_template, request, url_for

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET", "POST"])
def home():
    """Homepage"""
    return render_template("home.html", title="Home")
