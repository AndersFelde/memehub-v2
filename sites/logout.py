from flask import Blueprint, render_template, session, url_for, redirect
from modules.userAuth import validateUser
logout = Blueprint("logout", __name__, template_folder="templates",
                   static_folder="static")


@logout.route("/logout")
def page():
    if validateUser():
        session.pop("email", False)
        session.pop("user", False)
        session.pop("userId", False)
        session.pop("secret", False)

    return redirect(url_for("login.page"))
