from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "hello im behnam this is learning flask web-framework"