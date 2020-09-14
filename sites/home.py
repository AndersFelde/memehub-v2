from flask import Blueprint, render_template, session
from modules.content import content
from modules.userAuth import validateUser
home = Blueprint("home", __name__, template_folder="templates",
                 static_folder="static")


@home.route("/")
@home.route("/home")
def page():
    if validateUser():
        query = content()
        if "Error" not in query:
            return render_template("home.html", uploads=query)

        return render_template("home.html")
    else:
        return render_template("home.html")
