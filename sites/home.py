from flask import Blueprint, render_template, session
from modules.uploads import uploads
from modules.userAuth import validateUser
home = Blueprint("home", __name__, template_folder="templates",
                 static_folder="static")


@home.route("/")
@home.route("/home")
def page():
    if validateUser():
        upload = uploads()
        return render_template("home.html", uploads=upload)
        # content burde være objekt som har alle funksjoner og attributer innebygd, kan accesse den inni HTML

    else:
        return render_template("home.html")
