from datetime import datetime, timedelta
import csv
import os
from dotenv import load_dotenv
from fullmoon import IsFullMoon
import requests

url = "https://holidays.abstractapi.com/v1/"


def getBookings():
    bookings = []
    with open("bookings.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            bookings.append(row)
    return bookings


bookings = getBookings()
booking = []


class Room:
    def __init__(self, name, maxO, maxAge, minAge):
        self.name = name
        self.maxO = maxO
        self.maxAge = maxAge
        self.minAge = minAge


allTimes = [
    "09:00",
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
]
allRooms = [
    Room("Meeting", 200, 65, 18),
    Room("Moon", 18, 65, 26),
    Room("Food", 15, 117, 1),
    Room("Young Kids", 30, 12, 0),
    Room("Old Kids", 15, 18, 12),
    Room("Adults", 50, 65, 18),
    Room("Seniors", 65, 117, 65),
    Room("All Ages", 160, 117, 0),
]


def form1Checks(booking):
    # used in main.py
    # booking:Room object, date:datetime object, numOfPeople:int, length:int, age:int, name:str, phone:str
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
        errorMSG += "book with this age range, "
        passes = False
    if not maxOcc(booking[0], int(booking[2])):
        errorMSG += "have that many people in this room, "
        passes = False
    if not checkFullMoon(booking[0], booking[1]):
        errorMSG += "book not on a full moon, "
        passes = False
    return [passes, errorMSG[:-2]]


def form2Checks(booking):
    # used in main.py
    # booking:Room object, date:datetime object, numOfPeople:int, length:int, age:int, name:str, phone:str, time:str
    errorMSG = ""
    passes = True
    if not userBooked(booking[5], booking[6], booking[1], booking[7], bookings):
        errorMSG += "You already have a booking at this time, "
        passes = False
    if not checkTimeInAdvance(datetime.now(), booking[1], booking[7]):
        errorMSG += "You can't book less than 3 hours in advance, "
        passes = False
    return [passes, errorMSG[:2]]


def getRoom(roomName):
    # used in main.py
    # roomName:str
    for room in allRooms:
        if room.name == roomName:
            return room
    return False


def ageRange(room, age):
    # used in form1 checks
    # room:Room object, age:str
    for r in allRooms:
        if room.name == r.name:
            maxAge = r.maxAge
            minAge = r.minAge
            break
    minAgeIn, maxAgeIn = age.split("-")
    minAgeIn = int(minAgeIn)
    maxAgeIn = int(maxAgeIn)
    if minAgeIn >= minAge and maxAgeIn <= maxAge:
        return True
    else:
        return False


def maxOcc(room, numOfPeople):
    # used in form1 checks
    # room:Room object, numOfPeople:int
    for r in allRooms:
        if room.name == r.name:
            maxO = r.maxO
            break
    if numOfPeople > maxO:
        return False
    else:
        return True


def checkDayTimes(currentDate, date):
    # used in getAvaibleTimes
    # this checks the time of day, and returns the avaible times after that
    # date:datetime object, currentDate:datetime object, returns list of dates:str
    useTimes = []
    if date == currentDate.date():
        for i in allTimes:
            if int(currentDate.strftime("%H")) < int(i.split(":")[0]):
                useTimes.append(i)
        return useTimes
    else:
        return allTimes


def getAvabileTimes(date, room, length, bookings):
    # date:datetime.date object, room:Room object, length:str, bookings:list[list[str]]
    # used in main.py
    # compares times from checkDayTimes and the bookings already made
    meetLength = int(length.split()[0])
    usableTimes = checkDayTimes(datetime.now(), date)
    # usableTimes:list[str]

    # make lists of all booking for that day and room
    daysBookings = []
    for i in bookings:
        if i:
            if i[1] == date and i[0].name == room.name:
                daysBookings.append(i)

    if not daysBookings:
        if meetLength == 1:
            return usableTimes
        if meetLength == 2:
            return usableTimes[:9]
        if meetLength == 3:
            return usableTimes[:8]

    avaTimes = []
    addTime = True
    if meetLength == 1:
        for i in usableTimes:
            for j in daysBookings:
                if j[7] == i:
                    addTime = False
            if addTime:
                avaTimes.append(i)
            addTime = True
    elif meetLength == 2:
        for i in usableTimes[:9]:
            for j in daysBookings:
                if j[7] == i or j[7] == str(
                    (datetime.strptime(i, "%H:%M") + timedelta(hours=1)).strftime(
                        "%H:%M"
                    )
                ):
                    addTime = False
            if addTime:
                avaTimes.append(i)
            addTime = True
    elif meetLength == 3:
        for i in usableTimes[:8]:
            for j in daysBookings:
                if (
                    j[7] == i
                    or j[7]
                    == str(
                        (datetime.strptime(i, "%H:%M") + timedelta(hours=1)).strftime(
                            "%H:%M"
                        )
                    )
                    or j[7]
                    == str(
                        (datetime.strptime(i, "%H:%M") + timedelta(hours=2)).strftime(
                            "%H:%M"
                        )
                    )
                ):
                    addTime = False
            if addTime:
                avaTimes.append(i)
            addTime = True
    return avaTimes


def addBooking(booking):
    # date:datetime.date object, time:string
    d = open("bookings.csv", "a")
    for i in range(int(booking[3][0])):
        d.write("\n")
        lenght = str((int(str(booking[3][0])) - i)) + " hours"
        time = str(
            (datetime.strptime(booking[7], "%H:%M") + timedelta(hours=i)).strftime(
                "%H:%M"
            )
        )
        d.write(
            str(booking[0].name)
            + ","
            + str(booking[1])
            + ","
            + str(booking[2])
            + ","
            + lenght
            + ","
            + str(booking[4])
            + ","
            + str(booking[5])
            + ","
            + str(booking[6])
            + ","
            + time
        )

    d.close()
    # check this doesnt do anything
    getBookings()


def userBooked(name, phone, date, time, bookings):
    # used in form3 checks
    # date:datetime.date object, time:string, bookings:list[list[str]] , phone:string, name:string
    for booking in bookings:
        if (
            name == booking[5]
            and phone == booking[6]
            and date == booking[1]
            and time == booking[7]
        ):
            return False
    return True


def checkWeekend(date):
    # used in form1 checks
    # date:datetime.date object
    if date.weekday() > 4:
        print("Cannot book on the weekend")
        return False
    else:
        return True


def checkTimeInAdvance(now, dateS, bookingTime):
    # used in form2 checks
    # date:datetime.date object, bookingTime:string, now:datetime object
    minBookTime = now + timedelta(hours=3)
    bookingTime = datetime.strptime(bookingTime, "%H:%M")
    print(now.date(), type(dateS))
    print(minBookTime.time(), bookingTime.time())
    if now.date() == dateS and minBookTime.time() > bookingTime.time():
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
    # used in form1 checks
    # date:datetime.date object
    load_dotenv()
    country = "IE"
    day = date.day
    month = date.month
    year = date.year
    response = requests.get(
        url,
        params={
            "api_key": os.getenv("HOLIDAY_API"),
            "country": country,
            "year": year,
            "month": month,
            "day": day,
        },
    )
    print(response.text)
    if response.text == "[]":
        return True
    else:
        return False


def checkFullMoon(room, date):
    # used in form1 checks
    # date:datetime.date object, room:Room object

    date = datetime.strftime(date, "%Y-%m-%d")
    if room.name == "Moon":
        i = IsFullMoon()
        return i.set_date_string(date, "%Y-%m-%d").is_full_moon()
    else:
        return True
