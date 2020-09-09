from flask import Blueprint, render_template, request, session, url_for, redirect
user = Blueprint("user", __name__, template_folder="templates",
                 static_folder="static")


@user.route("/user", methods=["GET", "POST"])
def page():
    if session.get("email") == True:
        return render_template("user.html")
    else:
        return redirect(url_for("login.page"))
