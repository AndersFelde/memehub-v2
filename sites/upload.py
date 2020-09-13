from flask import Blueprint, render_template, session, request
import os
import binascii
from db.db import db
upload = Blueprint("upload", __name__, template_folder="templates",
                   static_folder="static")

allowed = {'png', 'jpg', 'jpeg'}

db = db()


def isAllowed(filename):
    ext = filename.split(".")[-1]
    if ext in allowed:
        return True
    else:
        return False


@upload.route("/upload", methods=['GET', 'POST'])
def page():
    if request.method == "POST":
        if isinstance(session.get("email"), str):
            if "file" in request.files:
                image = request.files["image"]
                if image.filename != "":
                    if isAllowed(image.filename):
                        filename = binascii.b2a_hex(os.urandom(
                            15)) + image.filename.split(".")[-1]
                        try:
                            db.fileUpload(image.filename, session["user"])
                        except:
                            pass
    else:
        return render_template("upload.html")
