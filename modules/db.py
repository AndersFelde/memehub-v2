import json
import mysql.connector
import binascii
import os
# ssh -L 3306:localhost:3306 servster


class db():
    def __init__(self):
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

    def login(self, email):
        try:
            self.cursor.execute("""SELECT passwd, username, userId, secret FROM users where email = %s""",
                                (email,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            return err, "Error"

    def signup(self, email, user, passwd):
        try:
            secret = binascii.b2a_hex(os.urandom(15))
            self.cursor.execute(
                """INSERT INTO users (email, username, passwd, secret) VALUES (%s, %s, %s, %s);""",
                (email, user, passwd, secret))
            self.con.commit()
            return self.cursor.rowcount, "record inserted"
        except mysql.connector.Error as err:
            return err, "Error"

    def fileUpload(self, filename, userId):
        try:
            self.cursor.execute(
                """INSERT INTO uploads (filename, userId) VALUES (%s, %s);""",
                (filename, userId))
            self.con.commit()
            return self.cursor.rowcount, "record inserted"
        except mysql.connector.Error as err:
            print(self.cursor.statement)
            return err, "Error"

    def userValidation(self, userId):
        try:
            self.cursor.execute("""SELECT secret FROM users where userId = %s""",
                                (userId,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            return err, "Error"
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
