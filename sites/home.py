from flask import Blueprint, render_template, session
home = Blueprint("home", __name__, template_folder="templates",
                 static_folder="static")


@home.route("/")
@home.route("/home")
def page():
    return render_template("home.html")
