from modules.db import db
from flask import session


class uploads():

    def __init__(self, userId=False):
        self.db = db()
        self.userId = userId
        self.content = self.getContent()
        self.userVotes = self.getUserVotes()
        self.amountVotes = self.getAmountVotes()
        print(self.amountVotes)

    def getContent(self):
        if not self.userId:
            query = self.db.getUploads()
        else:
            query = self.db.getUploadsByUser(self.userId)
        return query

    def getUserVotes(self):
        query = self.db.getUserVotes(session["userId"])
        userVoteDict = {}
        for row in query:
            userVoteDict[row[1]] = row[0]
        return userVoteDict

    def getAmountVotes(self):
        query = self.db.getAmountVotes()
        voteDict = {}
        for row in query:
            if row[0] in voteDict:
                voteDict[row[0]][row[1]] = row[2]
            else:
                voteDict[row[0]] = {row[1]: row[2]}
        return voteDict

    def setActive(self, uploadId, btnType):
        if uploadId in self.userVotes and btnType == self.userVotes[uploadId]:
            return "active-vote"
        return ""
