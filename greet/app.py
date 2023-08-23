from flask import Flask

app = Flask(__name__)


@app.get('/welcome')
def welcome():
    """incredible welcome message"""
    return f"<h1> Welcome </h1>"


@app.get('/welcome/home')
def welcome_home():
    """soothing return home"""
    return f"<h1> Welcome home </h1>"


@app.get('/welcome/back')
def welcome_back():
    """You're back!"""
    return f"<h1> Welcome back </h1>"
