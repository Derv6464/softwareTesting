import datetime
import constaints as c
from flask import Flask, request, render_template

app = Flask(__name__)
data = []
booking = []

@app.route('/')
def home():
    return render_template('home.html', data=[c.allRooms, c.allDates, c.allTimes], datetime=datetime)

@app.route('/submit_form1', methods=['POST', 'GET'])
def onSubmit():
    room = request.form['room']
    date = request.form['dateS']
    age = request.form['age']
    numOfPeople = request.form['numOfPpl']
    date = request.form['dateS']
    numOfPeople = request.form['numOfPpl']
    length = request.form['length']
    age = request.form['age']
    #do booking checks 
    
    tempBooking = [room, date, numOfPeople, length, age]
    formChecks = c.formChecks(tempBooking)
    if formChecks[0]:
        booking = tempBooking
        tempBooking = []
    else:
        pass
        #messege with error formChecks[1]

    print(booking)

    times = c.getAvabileTimes(date, room, c.getBookings())
    data.append([room, date])
    return render_template('selectTime.html', data=times)
    
@app.route('/submit_form2', methods=['POST', 'GET'])
def onTimeSubmit():
    time = request.form['time']
    #do booking checks
    booking.append(time)
    print(booking)
    c.addBooking(booking)
    booking = []
    return render_template('confirm.html', data=booking)

if __name__ == '__main__':
    app.run()