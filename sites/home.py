from flask import Blueprint, render_template, abort
homeS = Blueprint("home", __name__, template_folder="templates",
                  static_folder="static")


@homeS.route("/")
@homeS.route("/home")
def home():
    return render_template("home.html", user="joe")
