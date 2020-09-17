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


def checkFilename(filename):
    ext = filename.split(".")[-1]
    if ext in allowed:
        return True
    else:
        return False


def validateImage(request):
    if "image" in request.files:
        image = request.files["image"]
        if image.filename != "":
            if checkFilename(image.filename):
                return True
    return False


def randomString():
    return ''.join(random.choices(ascii_uppercase + digits, k=15))


@upload.route("/upload", methods=['GET', 'POST'])
def page():
    if request.method == "POST":
        if validateUser():
            if validateImage(request):
                image = request.files["image"]
                filename = randomString() + "." + image.filename.split(".")[-1]

                query = db.fileUpload(
                    filename, session["userId"])

                if "Error" not in query:
                    image.save(os.path.join("static\\uploads", filename))
                    return redirect(url_for("user.page"))

            # hvis bildet ikke ble validated
            flash("Det skjedde noe galt, prøv igjen")
            return render_template("upload.html")

        # hvis user ikke ble validated
        return(redirect(url_for("login.page")))

    else:
        if validateUser():
            return render_template("upload.html")
        return redirect(url_for("login.page"))
