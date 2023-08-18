import numpy as np
from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about-team")
def team():
    return render_template("about-team.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/project")
def project():
    return render_template("project.html")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)
