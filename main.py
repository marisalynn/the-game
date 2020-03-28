from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def game():
    return render_template('index.html', name='Marisa')