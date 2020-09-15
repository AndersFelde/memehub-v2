from modules.db import db
from flask import session

db = db()


def content(userId=False):
    if not userId:
        query = db.getUploads()
    else:
        query = db.getUploadsByUser(userId)

    votes = db.getUserVotes(session["userId"])
    return [query, votes]


def setActive(uploadId, btnType, query):
    for row in query:
        if uploadId == row[1] and btnType == row[0]:
            return "active-vote"
    return ""
