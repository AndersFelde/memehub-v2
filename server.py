from datetime import timedelta
from flask import Flask, render_template, session, request
import json
# sites
from sites.logout import logout
from sites.user import user
from sites.login import login
from sites.home import home
from sites.signup import signup

# hente creds


# db = db(mySqluser, mySqlpasswd)
# print(db.insert("users", "email, passwd, username", "'joe@joe.com', 'joe', 'joe'"))

site = Flask(__name__)

site.register_blueprint(home)
site.register_blueprint(login)
site.register_blueprint(user)
site.register_blueprint(logout)
site.register_blueprint(signup)

# with open("creds.json") as credsFile:
#     creds = json.load(credsFile)
#     key = creds["key"]

site.secret_key = "p6CVfomFtOhAb7pCuSXfBA"
site.permanent_session_lifetime = timedelta(days=7)


# # fikse sesion
# lage sign up / login
# sette opp db mysql eller sqlalchemy ?


if __name__ == "__main__":
    site.run(debug=True)
