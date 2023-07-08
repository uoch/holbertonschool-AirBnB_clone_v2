#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/states_list', strict_slashes=False)
def diplay():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)