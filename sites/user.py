from flask import Blueprint, render_template, request, session, url_for, redirect
user = Blueprint("user", __name__, template_folder="templates",
                 static_folder="static")


@user.route("/user", methods=["GET", "POST"])
def page():
    if checkLoggedIn():
        return render_template("user.html")
    else:
        return redirect(url_for("login.page"))


@user.route('/settings')
def settings():
    if checkLoggedIn():
        return render_template("user.html", settings=True)
    else:
        return redirect(url_for("login.page"))


def checkLoggedIn():
    sessionMail = session.get("email")
    if isinstance(sessionMail, str):
        return True
    else:
        print("joe")
        return False
