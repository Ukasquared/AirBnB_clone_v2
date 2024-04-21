#!/usr/bin/python3
""" create a minimal program
using flask the accept user input """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays on browser"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ displays on browser"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def user_input(text):
    """ recieves user input to display"""
    if '_' in text:
        text.replace('_', ' ')
    return (f"C {text}")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
