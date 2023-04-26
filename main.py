import datetime
import constaints as c
from flask import Flask, request, render_template

app = Flask(__name__)
data = []

@app.route('/')
def home():
    return render_template('home.html', data=[c.allRooms, c.allDates, c.allTimes])

@app.route('/submit_form1', methods=['POST', 'GET'])
def onSubmit():
    room = request.form['room']
    date = request.form['date']
    numOfPeople = request.form['numOfPeople']
    length = request.form['length']
    data.append([room, date])
    return render_template('selectTime.html', data=data)
    



if __name__ == '__main__':
    app.run()