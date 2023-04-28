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
    c.booking = []
    return render_template('home.html', data=c.allRooms, datetime=datetime)

@app.route('/submit_form1', methods=['POST', 'GET'])
def onSubmit():
    name = request.form['fName']
    phone = request.form['phoneN']
    room = request.form['room']
    date = request.form['dateS']
    age = request.form['age']
    numOfPeople = request.form['numOfPpl']
    length = request.form['length']
    #do booking checks 
    print(date)
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    room = c.getRoom(room)
    tempBooking = [room, date, numOfPeople, length, age, name, phone]
    formChecks = c.form1Checks(tempBooking)
    if formChecks[0]:
        c.booking = tempBooking
        print(booking)
        tempBooking = []
        times = c.getAvabileTimes(date, room,length, c.getBookings())
        return render_template('selectTime.html', data=times)
    else:
        flash(formChecks[1])
        return render_template('home.html', data=c.allRooms, datetime=datetime)

    
@app.route('/submit_form2', methods=['POST', 'GET'])
def onTimeSubmit():
    time = request.form['time']
    print(time)
    #do booking checks
    c.booking.append(time)
    print(c.booking)
    #c.addBooking(booking)
    return render_template('confirm.html', data=c.booking)

if __name__ == '__main__':
    app.run()