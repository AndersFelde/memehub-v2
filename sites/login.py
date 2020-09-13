from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from modules.db import db
from modules.userAuth import logUserIn
# from database import dbase as db

login = Blueprint("login", __name__, template_folder="templates",
                  static_folder="static")

db = db()

@login.route("/login", methods=["GET", "POST"])
def page():
    print(request.method)
    if request.method == "POST":
        email = request.form["email"]
        passwd = request.form["passwd"]

        if email != "" and passwd != "":
            login = logUserIn(email, passwd)
            if login[0]:
                return login[1]
            else:
                flash(login[1])
                return login[2]
        else:
            flash("Du kan ikke ha tomt brukernavn eller passord")
            return render_template("login.html", email=email)

    else:
        if isinstance(session.get("email"), str):
            return redirect(url_for("user.page"))
        return render_template("login.html")
