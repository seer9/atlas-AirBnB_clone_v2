#!/usr/bin/python3
"""this script starts a Flask web application that prints Hello HBNB!"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_PassedText_route(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_PassedText_route(text):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
