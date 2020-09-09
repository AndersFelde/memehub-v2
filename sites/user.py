from flask import Blueprint, render_template, request, session, url_for, redirect
user = Blueprint("user", __name__, template_folder="templates",
                 static_folder="static")


@user.route("/user", methods=["GET", "POST"])
def page():
    checkLoggedIn()
    return render_template("user.html")


@user.route('/settings')
def settings():
    if not checkLoggedIn():
        return render_template("user.html", settings=True)


def checkLoggedIn():
    print(session.get("email"))
    if session.get("email") == None:
        print("joe")
        return redirect(url_for("login.page"))
    else:
        return False
