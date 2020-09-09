from datetime import timedelta
from flask import Flask, render_template, session, request
from sites.home import home
from sites.login import login
from sites.user import user
from sites.logout import logout


site = Flask(__name__)
site.register_blueprint(home)
site.register_blueprint(login)
site.register_blueprint(user)
site.register_blueprint(logout)

site.secret_key = "JoeMama"
site.permanent_session_lifetime = timedelta(days=7)


# # fikse sesion
# lage sign up / login
# sette opp db mysql eller sqlalchemy ?


if __name__ == "__main__":
    site.run(debug=True)
