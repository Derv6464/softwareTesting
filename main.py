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
        times =[]
        times = c.getAvabileTimes(date, room,length, c.getBookings())
        print(times)
        return render_template('selectTime.html', data=times)
    else:
        flash(formChecks[1])
        return render_template('home.html', data=c.allRooms, datetime=datetime)

    
@app.route('/submit_form2', methods=['POST', 'GET'])
def onTimeSubmit():
    time = request.form['time']
    #do booking checks
        
    temp2Booking = c.booking
    temp2Booking.append(time)
    print(temp2Booking)
    formChecks = c.form2Checks(temp2Booking)
    if formChecks[0]:
        c.booking.append(time)
        print("testing")
        print(c.booking)
        temp2Booking = []
        c.addBooking(c.booking)
        return render_template('confirm.html', data=c.booking)
    else:
        flash(formChecks[1])
        times =[]
        times = c.getAvabileTimes(c.booking[1], c.booking[0],c.booking[3], c.getBookings())
        return render_template('selectTime.html', data=times)

if __name__ == '__main__':
    app.run()