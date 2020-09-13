from flask import Blueprint, flash, render_template, session, request, redirect, url_for
import random
from string import ascii_uppercase, digits
from modules.db import db
from modules.userAuth import validateUser
import os

upload = Blueprint("upload", __name__, template_folder="templates",
                   static_folder="static")

allowed = ('png', 'jpg', 'jpeg')

db = db()


def isAllowed(filename):
    ext = filename.split(".")[-1]
    if ext in allowed:
        return True
    else:
        return False


def randomString():
    return ''.join(random.choices(ascii_uppercase + digits, k=10))


@upload.route("/upload", methods=['GET', 'POST'])
def page():
    if request.method == "POST":
        if isinstance(session.get("email"), str) and validateUser():
            print(request.files)
            if "image" in request.files:
                image = request.files["image"]
                if image.filename != "":
                    if isAllowed(image.filename):
                        filename = randomString() + "." +\
                            image.filename.split(".")[-1]

                        query = db.fileUpload(
                            filename, session["userId"])

                        if "Error" not in query:
                            # try:
                            print(os.listdir())
                            image.save(os.path.join(
                                "static\\uploads", filename))
                            # except Error as err:
                            # flash("Fikk ikke lagra ass")
                            # return render_template("upload.html")
                            return redirect(url_for("user.page"))
                        else:
                            flash("Det skjedde noe galt, prøv igjen")
                            return render_template("upload.html")
                    else:
                        flash("Det bilde der er skjært ass")
                else:
                    flash("Kanskje ha et navn på bilde?")
            else:
                flash("Skjedde noe galt med bilde")
        else:
            return(redirect(url_for("login.page")))

        return render_template("upload.html")

    else:
        if isinstance(session.get("email"), str):
            return render_template("upload.html")
        return redirect(url_for("login.page"))
