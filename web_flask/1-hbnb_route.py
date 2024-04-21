#!/usr/bin/python3
""" a minimal program to test flask functionality"""
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


if __name__== "__main__":
    app.run(host='0.0.0.0')
