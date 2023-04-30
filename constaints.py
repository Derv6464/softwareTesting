import datetime
import csv

from fullmoon import IsFullMoon
import requests
url = "https://holidays.abstractapi.com/v1/"
api_key = "f9eb73a590b245259d9ecf7b8717445b"


moonAPI = "https://api.sunrise-sunset.org/json."

#csv order = Room,Date,Time,Age,Lenght,userID,bookingRef


def getBookings():
    bookings = []
    with open("bookings.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            bookings.append(row)
    return bookings

bookings = getBookings()
booking = []

class Room:
    def __init__(self,name, max, maxAge, minAge):
        self.name = name
        self.max = max
        self.maxAge = maxAge
        self.minAge = minAge

allTimes = ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
allDates = [(datetime.datetime.today() + datetime.timedelta(days=x)).strftime("%x") for x in range(7)]
allRooms = [Room("Meeting", 200, 65, 18), Room("Moon", 20, 46, 26), Room("Food", 15, 100, 1), Room("Young Kids", 30, 12, 0), Room("Old Kids", 15, 18, 12), Room("Adults", 50, 64, 18), Room("Seniors", 65, 100, 65), Room("All Ages", 160, 100, 0)]

class User:
    def __init__(self, booking, id, size, date):
        self.booking = booking
        self.id = id
        self.size = size
        self.date = date

def form1Checks(booking):
    errorMSG = "You can't: "
    passes = True
    if not checkWeekend(booking[1]):
        errorMSG += "book on weekends, "
        passes = False
    if not checkHoliday(booking[1]):
        errorMSG += "book on holidays, "
        passes = False
    if not checkNulls(booking):
        errorMSG += "leave any fields blank, "
        passes = False
    if not ageRange(booking[0], booking[4]):
        errorMSG += "book this room with your selected age range"
        passes = False
    if not maxOcc(booking[0], int(booking[2])):
        errorMSG += "have that many people in your selected room"
        passes = False
    return [passes,errorMSG[:-2]]

def form2Checks(booking):
    errorMSG = "You can't: "
    passes = True
    if not userBooked(booking[5], booking[6], booking[1], booking[2], bookings):
        errorMSG += "You already have a booking at this time"
        passes = False
    return [passes, errorMSG]
    

def getRoom(roomName):
    for room in allRooms:
        if room.name == roomName:
            return room
    return False

def ageRange(room, age):
    minAgeIn, maxAgeIn = age.split("-")
    minAgeIn = int(minAgeIn)
    maxAgeIn = int(maxAgeIn)
    if (minAgeIn >= room.minAge and maxAgeIn <= room.maxAge):
        return False
    else:
        return True


def maxOcc(room, numOfPeople):
    if (numOfPeople > room.max):
        return False
    else:
        return True
        
def getAvabileTimes(date, room, length ,bookings):
    meetLength =int(length.split()[0])

    #make lists of all booking on that day and room
    daysBookings = []
    for i in bookings:
        if i[1] == str(date) and i[0] == room.name:
            daysBookings.append(i)
    print(type(bookings[0][7]))
    if not daysBookings:
        return allTimes
    avaTimes = []
    addTime = True
    
    if meetLength ==1 :
        for i in allTimes:
            for j in daysBookings:
                if j[7] == i:
                    addTime = False
            if addTime:
                avaTimes.append(i)
            addTime = True
    #adding 1 ]/2 prob wont work cause date is a string in the csv
    elif meetLength == 2:
            for i in allTimes:
                for j in daysBookings:
                    if j[7] == i or j[7] == str((datetime.datetime.strptime(i,'%H:%M') + datetime.timedelta(hours=1)).strftime('%H:%M')):
                        addTime = False
                if addTime:
                    avaTimes.append(i)
                addTime = True
    elif meetLength == 3:
        for i in allTimes:
            for j in daysBookings:
                if j[7] == i or j[7] == str((datetime.datetime.strptime(i,'%H:%M') + datetime.timedelta(hours=1)).strftime('%H:%M')) or j[7] == str((datetime.datetime.strptime(i,'%H:%M') + datetime.timedelta(hours=2)).strftime('%H:%M')):
                    addTime = False
            if addTime:
                avaTimes.append(i)
    print(avaTimes)
    return avaTimes

def addBooking(booking):
    #include id if we do id, and make booking refrence
    d = open("bookings.csv", 'a')
    
    for i in range(int(booking[3][0])):
        d.write( "\n")
        d.write(str(booking[0].name) + "," + str(booking[1]) + "," + str(booking[2]) + "," + str(booking[3]) + "," + str(booking[4]) + "," + str(booking[5]) + "," + str(booking[6]+","+str((datetime.datetime.strptime(booking[7],'%H:%M') + datetime.timedelta(hours=i)).strftime('%H:%M'))))
    d.close()

    getBookings()
    

def checkValidId(id):
    return True
    
#tempBooking = [room, date, numOfPeople, length, age,time]
#csv order = Room,Date,Time,Age,Length,userID,bookingRef
#must be checked after second form is submited
def userBooked(name, phone, date, time, bookings) :
    for booking in bookings:
        if name == booking[5] and phone == booking[6] and date == booking[1] and time == booking[7]:
            return False
    return True

def checkMax(people):
    if people < Room.max:
        return False
    else:
        return True
    
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
    print("holiday api:" + response.text)
    if response.text == "[]" or response.text == '{"error":{"message":"You have exceeded the requests per second allowed by your current plan. Visit the Abstract dashboard to upgrade for a higher limit.","code":"too_many_requests","details":null}}': 
        return True
    else:
        return False
    
def checkFullMoon(date):
    i = IsFullMoon()
    date = str(date.date())
    return i.set_date_string(date, '%Y-%m-%d').is_full_moon()
