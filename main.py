import datetime

rooms = ["meeting", "moon", "food", "young kids", "old kids", "adults", "seniors", "all ages"]

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


def displayAllRooms(rooms):
    for room in rooms:
        print(room + " room")

displayAllRooms(rooms)

def book(room, time,id):
    bookingTime = datetime(hour=time, minute=0, second=0, microsecond=0)
    now = datetime.now()
    if not checkTime(time):
        return False
    if not checkValidId(id):
        return False
    
    
def checkTime(time):
    bookingTime = datetime(hour=time, minute=0, second=0, microsecond=0)
    eightOclock = datetime(hour=20, minute=0, second=0, microsecond=0)
    if bookingTime > eightOclock:
        print("Too late to book")
        return False

def checkValidId(id):
    if User.id != valid_id:
        return False
    
def checkDoubleBook():
    if Room.booked == True:
        print("Room already booked")
        return False
    
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
    

    