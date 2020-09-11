import json
import mysql.connector
# ssh -L 3306:localhost:3306 servster


class db():
    def __init__(self):
        # with open("creds.json") as credsFile:
        #     creds = json.load(credsFile)
        #     mySqlpasswd = creds["mysql"]["password"]
        #     mySqluser = creds["mysql"]["user"]

        # try:
        self.con = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="Jegeradmin",
            database="memehub",
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.con.cursor()
        # except mysql.connector.Error as err:
        #     print(err)

    def login(self, email):
        try:
            self.cursor.execute("""SELECT passwd, username FROM users where email = %s""",
                                (email,))
            print(self.cursor.statement)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(self.cursor.statement)
            return err, "Error"

    def signup(self, email, user, passwd):
        try:
            self.cursor.execute(
                """INSERT INTO users (email, username, passwd) VALUES (%s, %s, %s)""",
                (email, user, passwd))
            self.con.commit()
            print(self.cursor.statement)
            return self.cursor.rowcount, "record inserted"
        except mysql.connector.Error as err:
            print(self.cursor.statement)
            return err, "Error"

    def select(self, objects, table):
        try:
            self.cursor.execute("""SELECT %s FROM %s""",
                                (objects, table))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            return err, "Error"

    def where(self, objects, table, column, value):
        try:
            self.cursor.execute("""SELECT %s FROM %s where %s = %s""",
                                (objects, table, column, value))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(self.cursor.statement)
            return err, "Error"

    def insert(self, table, columns, values):
        try:
            self.cursor.execute(
                """INSERT INTO %s (%s) VALUES (%s)""", (table, columns, values))
            self.con.commit()
            return self.cursor.rowcount, "record inserted"
        except mysql.connector.Error as err:
            return err, "Error"
