from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome_greeting():
    'Displays Welcome html'
    return "<html><body><h1>Welcome!</h1></body></html>"


@app.route('/welcome/home')
def home_greeting():
    'Displays welcome home html'
    return "<html><body><h1>Welcome Home!</h1></body></html>"


@app.route('/welcome/back')
def back_greeting():
    'Displays welcome back html'
    return "<html><body><h1>Welcome back!</h1></body></html>"
