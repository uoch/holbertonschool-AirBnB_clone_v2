#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

"""The strict_slashes=False argument tells Flask to treat URLs
with or without a trailing slash as equivalent."""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    return "HBNB"


@app.route('/c/<text>')
def cfun(text):
    temp = text.replace("_", " ")
    return "c {}".format(temp)


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    temp = text.replace("_", " ")
    return "Python {}".format(temp)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
