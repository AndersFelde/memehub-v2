from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from modules.db import db
from modules.userAuth import logUserIn, validateUser
# from database import dbase as db

voter = Blueprint("voter", __name__)

db = db()


@voter.route("/api/voter", methods=["POST"])
def page():
    if validateUser():
        uploadId = request.form["uploadId"]
        btnType = int(request.form["btnType"])

        vote = db.getVote(session["userId"], uploadId)

        if "Error" not in vote:
            if len(vote) > 0:
                newVote = convertVote(btnType, int(vote[0][0]))
                if isinstance(newVote, int):
                    query = db.updateVote(session["userId"], uploadId, newVote)
                else:
                    query = db.delVote(session["userId"], uploadId)
                # reverse av vote
            else:
                query = db.insertVote(session["userId"], uploadId, btnType)

            if "Errror" not in query:
                return {"vote": "voted"}

        return {"Error": vote}


def convertVote(btnType, vote):
    print(btnType, vote)
    if btnType == vote:
        return "DEL"
    else:
        return int(not vote)
