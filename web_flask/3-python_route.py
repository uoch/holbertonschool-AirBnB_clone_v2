#!/usr/bin/python3

"""a script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    return "HBNB"


@app.route('"/c/<text>"')
def cfun(text):
    temp = text.replace("_", " ")
    return "c {}".format(temp)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    temp = text.replace("_", " ")
    return f"Python {temp}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
