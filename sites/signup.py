from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from modules.db import db
# from database import dbase as db

signup = Blueprint("signup", __name__, template_folder="templates",
                   static_folder="static")

db = db()


@signup.route("/signup", methods=["GET", "POST"])
def page():
    if request.method == "POST":
        email = request.form["email"]
        user = request.form["user"]
        passwd = request.form["passwd"]

        if passwd == "" or email == "" or user == "":
            flash("Du må fylle ut alle feltene", "error")
            return render_template("signup.html", email=email, user=user)

        query = db.signup(email, user, passwd)

        if "Error" not in query:
            session["email"] = email
            session["user"] = user
            return redirect(url_for("user.page"))
        else:
            print(query)
            flash("Brukernavnet eller mailen er allerede i bruk")
            return render_template("signup.html", email=email, username=user)

    else:
        if isinstance(session.get("email"), str):
            return redirect(url_for("user.page"))
        return render_template("signup.html")
