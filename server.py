from flask import Flask, render_template
from sites.home import homeS

site = Flask(__name__)
site.register_blueprint(homeS)
# # fikse sesion
# lage sign up / login
# sette opp db mysql eller sqlalchemy ?


if __name__ == "__main__":
    site.run(debug=True)
