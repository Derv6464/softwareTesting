import datetime
from flask import Flask, request, render_template

app = Flask(__name__)
data = []

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()