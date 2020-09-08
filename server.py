from flask import Flask, render_template
# from pages.home import home
site = Flask(__name__)
# # fikse sesion
# lage sign up / login
# sette opp db mysql eller sqlalchemy ?


@site.route("/")
def home():
    user = "joe"
    return render_template("base.html", user=user)


if __name__ == "__main__":
    site.run(debug=True)
