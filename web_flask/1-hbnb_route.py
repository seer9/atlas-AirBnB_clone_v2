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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
