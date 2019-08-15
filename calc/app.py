# Put your app in here.
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/add')
def add(a, b):
    """Add a and b."""
    a = request.args["a"]
    b = request.args["b"]

    return a + b


@app.route('/sub')
def sub(a, b):
    """Substract b from a."""

    return a - b


@app.route('/mult')
def mult(a, b):
    """Multiply a and b."""

    return a * b


@app.route('/div')
def div(a, b):
    """Divide a by b."""

    return a / b