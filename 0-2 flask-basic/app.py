from flask import Flask


app = Flask(__name__)


@app.route('/home')
@app.route('/behnam')
def index():
    name = "behnam"
    return f"hello {name}"

@app.route('/behnam2')
def index2():
    return "hello from behnam2"