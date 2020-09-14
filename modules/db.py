import json
import mysql.connector
import binascii
import os
from flask import session
# ssh -L 3306:localhost:3306 servster


class db():
    def connect(self):
        with open("creds.json") as credsFile:
            creds = json.load(credsFile)
            mySqlpasswd = creds["mysql"]["password"]
            mySqluser = creds["mysql"]["user"]

        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user=mySqluser,
                password=mySqlpasswd,
                database="memehub"
            )
            self.cursor = self.con.cursor()
        except mysql.connector.Error as err:
            print(err)

    def __query(self, execute):
        self.connect()
        try:
            if execute[0][:3] == "SEL" or execute[:3]:
                # fordi det kan være string eller tuple

                if isinstance(execute, tuple):
                    self.cursor.execute(execute[0], execute[1])
                else:
                    self.cursor.execute(execute)

                result = self.cursor.fetchall()
                self.con.close()
                return result
            else:
                self.cursor.execute(execute[0], execute[1])
                self.con.commit()
                self.con.close()
                return self.cursor.rowcount, "record inserted"
        except mysql.connector.Error as err:
            print(self.cursor.statement)
            return err, "Error"

    def login(self, email):
        return self.__query(("""SELECT passwd, username, userId, secret FROM users where email = %s""", (email,)))

    def signup(self, email, user, passwd):
        secret = binascii.b2a_hex(os.urandom(15))
        return self.__query(("""INSERT INTO users (email, username, passwd, secret) VALUES (%s, %s, %s, %s);""",
                             (email, user, passwd, secret)))

    def fileUpload(self, filename, userId):
        return self.__query(("""INSERT INTO uploads (filename, userId) VALUES (%s, %s);""", (filename, userId)))

    def userValidation(self, userId):
        return self.__query(("""SELECT secret FROM users where userId = %s""",
                             (userId,)))

    def getUploadsByUser(self, userId):
        return self.__query(("""SELECT uploads.filename, users.username from uploads join users on uploads.userId = users.userId
                            where uploads.userId = %s""",
                             (userId,)))

    def getUploads(self):
        return self.__query("SELECT uploads.filename, users.username from uploads join users on uploads.userId = users.userId")
        # ekstra tuple på slutten fordi man "må" ha det - billig løsning

    #         print(self.cursor.statement)

    # def select(self, objects, table):
    #     try:
    #         self.cursor.execute("""SELECT %s FROM %s""",
    #                             (objects, table))
    #         return self.cursor.fetchall()
    #     except mysql.connector.Error as err:
    #         return err, "Error"

    # def where(self, objects, table, column, value):
    #     try:
    #         self.cursor.execute("""SELECT %s FROM %s where %s = %s""",
    #                             (objects, table, column, value))
    #         return self.cursor.fetchall()
    #     except mysql.connector.Error as err:
    #         print(self.cursor.statement)
    #         return err, "Error"

    # def insert(self, table, columns, values):
    #     try:
    #         self.cursor.execute(
    #             """INSERT INTO %s (%s) VALUES (%s)""", (table, columns, values))
    #         self.con.commit()
    #         return self.cursor.rowcount, "record inserted"
    #     except mysql.connector.Error as err:
    #         return err, "Error"
