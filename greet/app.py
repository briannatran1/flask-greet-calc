from flask import Flask

app = Flask(__name__)


@app.get('/welcome')
def welcome():

    return f"<h1> Welcome </h1>"


@app.get('/welcome/home')
def welcome_home():

    return f"<h1> Welcome home </h1>"


@app.get('/welcome/back')
def welcome_back():

    return f"<h1> Welcome back </h1>"
