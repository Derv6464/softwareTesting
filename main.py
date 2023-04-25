import datetime
import csv

def getBookings():
    bookings = []
    with open("bookings.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            bookings.append(row)
    return bookings

allRooms = ["meeting", "moon", "food", "young kids", "old kids", "adults", "seniors", "all ages"]
allTimes = ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
#can only book a date make 1 week in adavance (i week of dates avaible to book), date format: mm/dd/yy
allDates = [(datetime.datetime.today() + datetime.timedelta(days=x)).strftime("%x") for x in range(7)]

class Room:
    def __init__(self,name, booked, max, time):
        self.booked = booked
        self.name = name
        self.max = max
        self.time = time

class User:
    def __init__(self, booking, id, size):
        self.booking = booking
        self.id = id
        self.size = size

def selectAllRooms():
    print("Please select a room to book:\t(number input)")
    for i in range(1,len(allRooms)):
        print("["+str(i)+"] "+allRooms[i] + " room")
    
    return int(input())

def selctAllDates():
    print("Please select a date to book:\t(number input)")
    for i in range(1,len(allDates)):
        print("["+str(i)+"] "+allDates[i])
    
    return int(input())

def selectAvabileTimes(date,room,bookings):
    print("Please select a time to book:\t(number input)")
    avaTimes = []
    for i in allTimes:
        for j in bookings:
            if j[2] != date and j[1] != room and j[3] != i:
                avaTimes.append(i)
    
    for i in range(1,len(avaTimes)):
        print("["+str(i)+"] "+avaTimes[i])
    return avaTimes,int(input())


def makeSelection():
    room = allRooms[selectAllRooms()]
    date = allDates[selctAllDates()]
    timeSelection = selectAvabileTimes(date,room,getBookings())
    time = timeSelection[0][timeSelection[1]]
    return room, time, date

def addBooking(booking):
    with open("bookings.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(booking)
    getBookings()

def book(room, time,id):
    bookingTime = datetime(hour=time, minute=0, second=0, microsecond=0)
    now = datetime.now()
    #if not checkTime(time):
    #    return False
    #if not checkValidId(id):
    #    return False
    
    #if checks passes
    addBooking(makeSelection(allRooms,allTimes,allDates))
    
#def checkTime(time):
#    bookingTime = datetime(hour=time, minute=0, second=0, microsecond=0)
#    eightOclock = datetime(hour=20, minute=0, second=0, microsecond=0)
#    if bookingTime > eightOclock:
#        print("Too late to book")
#        return False

def checkValidId(id):
    if User.id != valid_id:
        return False
    
#def checkDoubleBook():
#    if Room.booked == True:
#        print("Room already booked")
#        return False
    
def userBooked():
    if User.booking == True:
        print("You already have a booking")
        return False

def checkMax():
    if User.size < Room.max:
        print("This room has insufficient space")
        return False
def checkWeekend():
    now = datetime.now()
    if now.weekday() > 4:
        print("Cannot book on weekend")
        return False
    
def checkTimeInAdvance(now,bookingTime):
    if now + 3 < bookingTime:
        print("Must book 3 hours in advance")
        return False
    

    