from flask import Blueprint, render_template, session, url_for, redirect
logout = Blueprint("logout", __name__, template_folder="templates",
                   static_folder="static")


@logout.route("/logout")
def logoutS():
    if session["email"]:
        session.pop("email", False)
        session.pop("user", False)
        session.pop("userId", False)

    return redirect(url_for("login.page"))
