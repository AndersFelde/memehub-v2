from flask import Blueprint, render_template, request, session, url_for, redirect
from modules.userAuth import validateUser
from modules.uploads import uploads
user = Blueprint("user", __name__, template_folder="templates",
                 static_folder="static")


@user.route("/user")
def page():
    if validateUser():
        upload = uploads(session["userId"])
        return render_template("user.html", uploads=upload)
    else:
        return redirect(url_for("login.page"))


@user.route('/settings')
def settings():
    if validateUser():
        return render_template("user.html", settings=True)
    else:
        return redirect(url_for("login.page"))


# def checkLoggedIn():
#     sessionMail = session.get("email")
#     if isinstance(sessionMail, str):
#         return True
#     else:
#         print("joe")
#         return False
