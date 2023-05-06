import datetime


def checkTimeInAdvance(date, bookingTime):
    #check this tommorow !!!!!!!
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    now = datetime.datetime.now()
    minBookTime = (now + datetime.timedelta(hours=3))
    bookingTime = datetime.datetime.strptime(bookingTime,'%H:%M')
    print(minBookTime.date())
    print(date.date())
    if minBookTime.date() == date.date() and minBookTime.time() > bookingTime.time():
        print("Must book 3 hours in advance")
        return False
    else:
        return True
    
checkTimeInAdvance((datetime.datetime.now()).strftime('%Y-%m-%d'),(datetime.datetime.now() + datetime.timedelta(hours = 2)).strftime("%H:%M"))