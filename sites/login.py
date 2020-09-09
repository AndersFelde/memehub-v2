from flask import Blueprint, render_template, request, session, url_for, redirect, flash
login = Blueprint("login", __name__, template_folder="templates",
                  static_folder="static")


@login.route("/login", methods=["GET", "POST"])
def page():
    if request.method == "POST":
        email = request.form["email"]
        passwd = request.form["passwd"]
        session["email"] = email

        if passwd == "":
            flash("Du kan ikke ha blankt passord", "error")
            return render_template("login.html")

        session["passwd"] = passwd
        return redirect(url_for("user.page"))
    else:
        if session.get("email") == False:
            return redirect(url_for("user.page"))
        return render_template("login.html")
