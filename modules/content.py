from modules.db import db
from modules.userAuth import validateUser
db = db()


def content(userId=False):
    if not userId:
        query = db.getUploads()
    else:
        query = db.getUploadsByUser(userId)
    return query
