import datetime
import csv
import requests
url = "https://holidays.abstractapi.com/v1/"
api_key = "f9eb73a590b245259d9ecf7b8717445b"


def getBookings():
    bookings = []
    with open("bookings.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            bookings.append(row)
    return bookings

bookings = getBookings()
#allRooms = ["Meeting", "Moon", "Food", "Young Kids", "Old Kids", "Adults", "Seniors", "All Ages"]
maxOccupancy =[]
allTimes = ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
#can only book a date make 1 week in adavance (i week of dates avaible to book), date format: mm/dd/yy
allDates = [(datetime.datetime.today() + datetime.timedelta(days=x)).strftime("%x") for x in range(7)]
allRooms = [Room("Meeting", 200, 65, 18), Room("Moon", 20, 46, 26), Room("Food", 15, 100, 1), Room("Young Kids", 30, 12, 0), Room("Old Kids", 15, 18, 12), Room("Adults", 50, 64, 18), Room("Seniors", 65, 100, 65), Room("All Ages", 160, 0, 100)]
class Room:
    def __init__(self,name, max, maxAge):
        self.name = name
        self.max = max
        self.maxAge = maxAge
        self.minAge = minAge

class User:
    def __init__(self, booking, id, size, date):
        self.booking = booking
        self.id = id
        self.size = size
        self.date = date

def formChecks(booking):
    pass

def getRoom(roomName):
    for room in allRooms:
        if room.name == roomName:
            return room
    return False

def ageRange(room, age):
    for item in allRooms:
        if item.name == room:
            if age < item.maxAge:
                return True
            else:
                return False



def getAvabileTimes(date,room,bookings):
    avaTimes = []
    for i in allTimes:
        for j in bookings:
            if j[2] != date and j[1] != room and j[3] != i:
                avaTimes.append(i)
    return avaTimes


def makeSelection():
    room = allRooms[selectAllRooms()]
    date = allDates[selctAllDates()]
    timeSelection = selectAvabileTimes(date,room,getBookings())
    time = timeSelection[0][timeSelection[1]]
    return room, time, date

def addBooking(booking):
    #include id if we do id, and make booking refrence
    with open("bookings.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(booking)
    getBookings()

def book(room, time,id):
    bookingTime = datetime.datetime(hour=time, minute=0, second=0, microsecond=0)
    now = datetime.datetime.now()
    #if not checkTime(time):
    #    return False
    #if not checkValidId(id):
    #    return False
    
    #if checks passes
    addBooking(makeSelection(allRooms,allTimes,allDates),id)
    
#def checkTime(time):
#    bookingTime = datetime(hour=time, minute=0, second=0, microsecond=0)
#    eightOclock = datetime(hour=20, minute=0, second=0, microsecond=0)
#    if bookingTime > eightOclock:
#        print("Too late to book")
#        return False

def checkValidId(id):
    return True
    
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
    return True 
    
def checkHoliday(date):
    country = "IE"
    day = date.day
    month = date.month
    year = date.year
    response = requests.get(url, params={"api_key": api_key, "country": country, "year": year, "month": month, "day": day})
    if response: 
        return False
    else:
        return True