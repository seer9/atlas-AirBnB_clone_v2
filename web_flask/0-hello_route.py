#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)



"""this script starts a Flask web application that prints Hello HBNB!"""
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)