import datetime
import csv
import requests
url = "https://holidays.abstractapi.com/v1/"
api_key = "f9eb73a590b245259d9ecf7b8717445b"

#csv order = Room,Date,Time,Age,Lenght,userID,bookingRef

def getBookings():
    bookings = []
    with open("bookings.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            bookings.append(row)
    return bookings

bookings = getBookings()

class Room:
    def __init__(self,name, max, maxAge,minAge):
        self.name = name
        self.max = max
        self.maxAge = maxAge
        self.minAge = minAge

#allRooms = ["Meeting", "Moon", "Food", "Young Kids", "Old Kids", "Adults", "Seniors", "All Ages"]
maxOccupancy =[]
allTimes = ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
#can only book a date make 1 week in adavance (i week of dates avaible to book), date format: mm/dd/yy
allDates = [(datetime.datetime.today() + datetime.timedelta(days=x)).strftime("%x") for x in range(7)]
allRooms = [Room("Meeting", 200, 65, 18), Room("Moon", 20, 46, 26), Room("Food", 15, 100, 1), Room("Young Kids", 30, 12, 0), Room("Old Kids", 15, 18, 12), Room("Adults", 50, 64, 18), Room("Seniors", 65, 100, 65), Room("All Ages", 160, 100, 0)]

class User:
    def __init__(self, booking, id, size, date):
        self.booking = booking
        self.id = id
        self.size = size
        self.date = date

def form1Checks(booking):
    errorMSG = "You can't:"
    passes = True
    if not checkWeekend(booking[1]):
        errorMSG += "book on weekends,"
        passes = False
    if not checkHoliday(booking[1]):
        errorMSG += "book on holidays,"
        passes = False
    if not checkNulls(booking):
        errorMSG += "leave any fields blank,"
        passes = False
    return [passes,errorMSG]

def form2Checks(booking):
    if not userBooked(booking, bookings):
        return [False, "You already have a booking at this time"]
    

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

def addBooking(booking):
    #include id if we do id, and make booking refrence
    with open("bookings.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(booking)
    getBookings()
    

def checkValidId(id):
    return True
    
#tempBooking = [room, date, numOfPeople, length, age,time]
#csv order = Room,Date,Time,Age,Lenght,userID,bookingRef
#must be checked after second form is submited
def userBooked(booking, bookings):
    for i in bookings:
        if i[0] == booking[0].name and i[1] == booking[1] and i[3] == booking[5]:
            return False
    return True

def checkMax():
    if User.size < Room.max:
        print("This room has insufficient space")
        return False
    
def checkWeekend(date):
    if date.weekday() > 4:
        print("Cannot book on weekend")
        return False
    else:
        return True
    
def checkTimeInAdvance(now,bookingTime):
    if now + 3 < bookingTime:
        print("Must book 3 hours in advance")
        return False
    return True 

def checkNulls(booking):
    for i in booking:
        if i == "":
            return False
    return True
    
def checkHoliday(date):
    country = "IE"
    day = date.day
    month = date.month
    year = date.year
    response = requests.get(url, params={"api_key": api_key, "country": country, "year": year, "month": month, "day": day})
    print(response)
    decoded_response = response.text
    print(type(decoded_response))
    if response.text != "[]": 
        return False
    else:
        return True