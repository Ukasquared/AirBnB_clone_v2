#!/usr/bin/python3
""" create a minimal program
using flask the accept user input """
from flask import Flask, render_template
from models import storage
from models.state import State
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
        text = text.replace('_', ' ')
    return (f"C {text}")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def second_input(text):
    if "_" in text:
        text = text.replace('_', ' ')
    return (f"Python {text}")


@app.route('/number/<int:n>', strict_slashes=False)
def accept_int(n):
    return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def serve_html(n):
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def serve_odd_or_even(n):
    return (render_template('6-number_odd_or_even.html', n=n))


@app.teardown_appcontext
def close_session(exception):
    """ closes a thread """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ list the states """
    states = storage.all(State)
    return (render_template('7-states_list.html', states=states))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
