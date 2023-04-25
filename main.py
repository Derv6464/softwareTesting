import datetime
import constaints as c
from flask import Flask, request, render_template

app = Flask(__name__)
data = []

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()