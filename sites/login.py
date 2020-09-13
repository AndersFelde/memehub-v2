from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from modules.db import db
# from database import dbase as db

login = Blueprint("login", __name__, template_folder="templates",
                  static_folder="static")

db = db()

# lage login som standalone module


def logUserIn(email, passwd):
    if passwd == "" or email == "":
            flash("Du kan ikke ha blankt passord, eller email", "error")
            return render_template("login.html", email=email)

        query = db.login(email)

        if "Error" not in query:
            if len(query) > 0:
                queryPasswd = query[0][0]
                if passwd == queryPasswd:
                    session["email"] = email
                    session["user"] = query[0][1]
                    session["userId"] = query[0][2]
                    print(session)
                    return redirect(url_for("user.page"))
                else:
                    print(query)
                    flash("Epost eller passord er feil")
                    return render_template("login.html", email=email)
            else:
                print(query)
                flash("Epost eller passord er feil")
                return render_template("login.html", email=email)
        else:
            print(query)
            flash("Det skjedde noe galt, vennligst prøv igjen")
            return render_template("login.html", email=email)


@login.route("/login", methods=["GET", "POST"])
def page():
    print(request.method)
    if request.method == "POST":
        email = request.form["email"]
        passwd = request.form["passwd"]
        
        return logUserIn(email, passwd)

        

    else:
        if isinstance(session.get("email"), str):
            return redirect(url_for("user.page"))
        return render_template("login.html")
