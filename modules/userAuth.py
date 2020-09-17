from flask import session, redirect, url_for, render_template
from modules.db import db
import binascii

db = db()


def logUserIn(email, passwd):
    query = db.login(email)

    if "Error" not in query and len(query) > 0:
        queryPasswd = query[0][0]
        if passwd == queryPasswd:
            session["email"] = email
            session["user"] = query[0][1]
            session["userId"] = query[0][2]
            session["secret"] = query[0][3]
            print(session)
            return (True, redirect(url_for("user.page")))
        else:
            print(query)
            return (False, "Epost eller passord er feil", redirect(url_for("login.page")))
    else:
        print(query)
        return (False, "Epost eller passord er feil", redirect(url_for("login.page")))


def __checkSession():
    if "userId" in session:
        if isinstance(session["userId"], int):
            return True
    return False


def validateUser():

    if not __checkSession():
        return False

    userId = session["userId"]
    query = db.userValidation(userId)
    if "Error" not in query and len(query) > 0:
        if session["secret"] == query[0][0]:
            print(f"Validated user: {userId}")
            return True
    return False
