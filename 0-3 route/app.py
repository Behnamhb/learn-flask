from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> hello world </h1>"

@app.route('/login/<path:name>')
def login(name):
    return f"<h1>welcome {name}</h1>"