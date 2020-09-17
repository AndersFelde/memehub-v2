from datetime import timedelta
from flask import Flask, render_template, session, request
import json
# sites
from sites.logout import logout
from sites.user import user
from sites.login import login
from sites.home import home
from sites.signup import signup
from sites.upload import upload
from sites.api.voter import voter

# hente creds


# db = db(mySqluser, mySqlpasswd)
# print(db.insert("users", "email, passwd, username", "'joe@joe.com', 'joe', 'joe'"))

site = Flask(__name__)

site.register_blueprint(home)
site.register_blueprint(login)
site.register_blueprint(user)
site.register_blueprint(logout)
site.register_blueprint(signup)
site.register_blueprint(upload)
site.register_blueprint(voter)

with open("creds.json") as credsFile:
    creds = json.load(credsFile)
    key = creds["key"]

site.secret_key = key
site.permanent_session_lifetime = timedelta(days=7)

site.config['UPLOAD_FOLDER'] = "static\\uploads"
UPLOADED_FILES_DEST = "static\\uploads"
UPLOADS_DEFAULT_DEST = "static\\uploads"
# # fikse sesion
# lage sign up / login
# sette opp db mysql eller sqlalchemy ?


if __name__ == "__main__":
    site.run(debug=True)
