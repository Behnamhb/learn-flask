from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loop')
def loop():
    costumers = ['ali', 'hasan', 'naghi']
    numbers = [ i for i in range(10)]
    return render_template('loop.html', costumers=costumers, numbers=numbers)