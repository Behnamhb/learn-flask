from flask import Flask, render_template
import random


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/result/')
def heads_tails():
    heads_tails = random.randint(1,2)
    return render_template('result.html', heads_or_tails=heads_tails)