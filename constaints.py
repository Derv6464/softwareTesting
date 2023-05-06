import datetime
import csv
import os
from dotenv import load_dotenv
from fullmoon import IsFullMoon
import requests
url = "https://holidays.abstractapi.com/v1/"
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
    def __init__(self,name, maxO, maxAge, minAge):
        self.name = name
        self.maxO = maxO
        self.maxAge = maxAge
        self.minAge = minAge

allTimes = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
allDates = [(datetime.datetime.today() + datetime.timedelta(days=x)).strftime("%x") for x in range(7)]
allRooms = [Room("Meeting", 200, 65, 18), Room("Moon", 18, 65, 26), Room("Food", 15, 100, 1), Room("Young Kids", 30, 12, 0), Room("Old Kids", 15, 18, 12), Room("Adults", 50, 65, 18), Room("Seniors", 65, 117, 65), Room("All Ages", 160, 117, 0)]

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
        errorMSG += "book with this age range"
        passes = False
    if not maxOcc(booking[0], int(booking[2])):
        errorMSG += "have that many people in this room"
        passes = False
    if not checkFullMoon(booking[0],booking[1]):
        errorMSG += "book not on a full moon"
        passes = False
    
    return [passes,errorMSG[:-2]]

def form2Checks(booking):
    errorMSG = "You can't: "
    passes = True
    if not userBooked(booking[5], booking[6], booking[1], booking[7], bookings):
        errorMSG += "You already have a booking at this time"
        passes = False
    if not checkTimeInAdvance(booking[1],booking[7]):
        errorMSG += "book less than 3 hours in advance"
        passes = False
    return [passes, errorMSG]
    

def getRoom(roomName):
    for room in allRooms:
        if room.name == roomName:
            return room
    return False

def ageRange(room, age):
    for r in allRooms:
        if room == r.name:
            maxAge = r.maxAge
            minAge = r.minAge
            break
    minAgeIn, maxAgeIn = age.split("-")
    minAgeIn = int(minAgeIn)
    maxAgeIn = int(maxAgeIn)
    if (minAgeIn >= minAge and maxAgeIn <= maxAge):
        return True
    else:
        return False


def maxOcc(room, numOfPeople):
    for r in allRooms:
        if room == r.name:
            maxO = r.maxO
            break
    if (numOfPeople > maxO):
        return False
    else:
        return True
    
def checkDayTimes(currentDate, date):
    useTimes = []
    #currentDate = datetime.datetime.now()
    if date == currentDate.date():
        for i in allTimes:
            if int(currentDate.strftime("%H")) < int(i.split(":")[0]):
                useTimes.append(i)
        return useTimes
    else:
        return allTimes
        
def getAvabileTimes(date, room, length ,bookings):
    meetLength =int(length.split()[0])
    usableTimes = checkDayTimes(datetime.datetime.now(), date)
    #make lists of all booking on that day and room
    daysBookings = []
    for i in bookings:
        if i:
            if i[1] == str(date) and i[0] == room.name:
                daysBookings.append(i)
    
    if not daysBookings:
        return usableTimes
    avaTimes = []
    addTime = True

    if meetLength ==1 :
        for i in usableTimes:
            for j in daysBookings:
                if j[7] == i:
                    addTime = False
            if addTime:
                avaTimes.append(i)
            addTime = True
    elif meetLength == 2:
            for i in usableTimes:
                for j in daysBookings:
                    if j[7] == i or j[7] == str((datetime.datetime.strptime(i,'%H:%M') + datetime.timedelta(hours=1)).strftime('%H:%M')):
                        addTime = False
                if addTime:
                    avaTimes.append(i)
                addTime = True
    elif meetLength == 3:
        for i in usableTimes:
            for j in daysBookings:
                if j[7] == i or j[7] == str((datetime.datetime.strptime(i,'%H:%M') + datetime.timedelta(hours=1)).strftime('%H:%M')) or j[7] == str((datetime.datetime.strptime(i,'%H:%M') + datetime.timedelta(hours=2)).strftime('%H:%M')):
                    addTime = False
            if addTime:
                avaTimes.append(i)
    return avaTimes

def addBooking(booking):
    with open('bookings.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(booking)

    getBookings()
   
#tempBooking = [room, date, numOfPeople, length, age,time]
#csv order = Room,Date,Time,Age,Length,userID,bookingRef
#must be checked after second form is submited
def userBooked(name, phone, date, time, bookings) :

    for booking in bookings:
        if name == booking[5] and phone == booking[6] and date.strftime("%Y-%m-%d") == booking[1] and time == booking[7]:
            return False
    return True
   
def checkWeekend(date):
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    if date.weekday() > 4:
        print("Cannot book on the weekend")
        return False
    else:
        return True
    

def checkTimeInAdvance(date, bookingTime):
    #check this tommorow !!!!!!!
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    now = datetime.datetime.now()
    minBookTime = (now + datetime.timedelta(hours=3))
    bookingTime = datetime.datetime.strptime(bookingTime,'%H:%M')
    if now.date() == date.date() and minBookTime.time() > bookingTime.time():
        print("Must book 3 hours in advance")
        return False
    else:
        return True

def checkNulls(booking):
    for i in booking:
        if i == "":
            return False
    return True
    
def checkHoliday(date):
    load_dotenv()
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    country = "IE"
    day = date.day
    month = date.month
    year = date.year
    response = requests.get(url, params={"api_key": os.getenv("HOLIDAY_API"), "country": country, "year": year, "month": month, "day": day})
    print(response.text)
    #if response.status_code!=200:
    #    return True
    if response.text == "[]": 
        return True
    else:
        return False
    
def checkFullMoon(room,date):
    if room == "Moon":
        i = IsFullMoon()
        return i.set_date_string(date, '%Y-%m-%d').is_full_moon()
    else:
        return True