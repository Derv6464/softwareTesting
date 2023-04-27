import datetime
import constaints as c
from flask import Flask, request, render_template

app = Flask(__name__)
data = []

@app.route('/')
def home():
    return render_template('home.html', data=[c.allRooms, c.allDates, c.allTimes], datetime=datetime)

@app.route('/submit_form1', methods=['POST', 'GET'])
def onSubmit():
    room = request.form['room']
    date = request.form['dateS']
    age = request.form['age']
    numOfPeople = request.form['numOfPpl']
    length = request.form['length']
    data.append([room, date])
    return render_template('selectTime.html', data=[c.allRooms, c.allDates, c.allTimes])


if __name__ == '__main__':
    app.run()