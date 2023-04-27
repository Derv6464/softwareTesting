import datetime
import constaints as c
from flask import Flask, request, render_template, flash

#csv order = Room,Date,Time,Age,Lenght,userID,bookingRef

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
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

    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    room = c.getRoom(room)
    tempBooking = [room, date, numOfPeople, length, age]
    formChecks = c.form1Checks(tempBooking)
    if formChecks[0]:
        booking = tempBooking
        tempBooking = []
        times = c.getAvabileTimes(date, room, c.getBookings())
        return render_template('selectTime.html', data=times)
    else:
        flash(formChecks[1])
        return render_template('home.html', data=[c.allRooms, c.allDates, c.allTimes], datetime=datetime)

    
@app.route('/submit_form2', methods=['POST', 'GET'])
def onTimeSubmit():
    time = request.form['time']
    print(time)
    #do booking checks
    booking.append(time)
    print(booking)
    #c.addBooking(booking)
    return render_template('confirm.html', data=booking)

if __name__ == '__main__':
    app.run()