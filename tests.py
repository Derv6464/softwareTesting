import csv
import datetime



def getBookings():
    bookings = []
    with open("bookings.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            bookings.append(row)

#list of all rooms and times
allRooms = ["meeting", "moon", "food", "young kids", "old kids", "adults", "seniors", "all ages"]
allTimes = ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
#can only book a date make 1 week in adavance (i week of dates avaible to book), date format: mm/dd/yy
allDates = [(datetime.datetime.today() + datetime.timedelta(days=x)).strftime("%x") for x in range(7)]

def selectAllRooms(rooms):
    print("Please select a room to book:\t(number input)")
    for i in range(1,len(rooms)):
        print("["+str(i)+"] "+rooms[i] + " room")
    
    return int(input())

def displayAllDates(times):
    print("Please select a date to book:\t(number input)")
    for i in range(1,len(times)):
        print("["+str(i)+"] "+times[i])
    
    return int(input())

def displayAvabileTimes(date,room,times,bookings):
    print("Please select a time to book:\t(number input)")
    avaTimes = []
    for i in times:
        for j in bookings:
            if j[2] != date and j[1] != room and j[3] != i:
                avaTimes.append(i)
    
    for i in range(1,len(avaTimes)):
        print("["+str(i)+"] "+avaTimes[i])
    return int(input())


def makeSelection(rooms,times,dates):
    room = rooms[selectAllRooms(rooms)]
    date = dates[displayAllDates(dates)]
    time = times[displayAvabileTimes(date,room,times,bookings)]
    return room, time, date

def addBooking(booking):
    with open("bookings.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(booking)
    getBookings()



addBooking(makeSelection(allRooms,allTimes,allDates))
print(bookings)