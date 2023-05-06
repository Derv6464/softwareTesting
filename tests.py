import csv
import unittest
from unittest import mock
import datetime
import shutil
import time
import constaints as c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TestStringMethods(unittest.TestCase):

    #Setup for testing
    def setUp(self):
        self.Christmas = '2023-12-25'
        self.fullMoon = '2023-3-7'
        #name, phone, date, time, bookings
        self.Tester = c.User(True, 10, 10, self.Christmas)
        self.TestRoom = c.Room("Meeting",6,100,0)
        self.TestFood = c.Room("Food", 15, 100, 1)
        self.TestMoonRoom = c.Room("Moon",6,100,0)
        self.allRooms = c.allRooms
        self.allTimes = c.allTimes
        self.bookings = [
            ["Meeting", '2023-04-15', 11, "1 hours", 44, 'John', '0123456789', '13:00'],
            ["Moon", '2023-04-17', 7, "2 hours", 30, 'Jane', '9876543210', '14:00'],
            ["Meeting", '2023-04-16',22, "1 hours", 60, 'Bob', '0123456789', '15:00']
        ]
        self.newBookingOne = ["Meeting", '2023-04-17', 100, "1 hours", "20-40", 'Jane', '9876543210', '14:00']
        self.newBookingTwo = ["Meeting", '2023-04-16', 60, "1 hours", "20-40", 'Bob', '9876543210', '14:00']
        self.newBookingThree = ["Meeting", '2023-06-17', 60, "1 hours", "20-40", 'Bob', '9876543210', '14:00']
        self.newBookingNulls = ["", '2023-04-17', 25, "1 hours", "20-40", 'Bob', '9876543210', '14:00']
        self.newBookingMax = ["Food", '2023-04-17', 60, "1 hours", "20-40", 'Sarah', '9876543210', '14:00']
    
    #api testing
    def test_checkHoliday(self):
        # check to ensure that the function returns false when the date is a holiday
        self.assertEqual(c.checkHoliday(self.Christmas), False)
        time.sleep(5)
        # check to ensure that the function returns true when the date isn't a holiday
        self.assertEqual(c.checkHoliday(self.newBookingOne[1]), True)

    def test_userBooked(self):
        #check to ensure that the function returns False when the user already has a booking
        self.assertEqual(c.userBooked(self.newBookingOne[5], self.newBookingOne[6], datetime.datetime.strptime(self.newBookingOne[1], "%Y-%m-%d"), self.newBookingOne[7], self.bookings),False)
        #check to ensure that the function returns true when the user doesnt already have a booking
        self.assertEqual(c.userBooked(self.newBookingTwo[5], self.newBookingTwo[6], datetime.datetime.strptime(self.newBookingTwo[1], "%Y-%m-%d"), self.newBookingTwo[7], self.bookings),True)
 

    def test_checkWeekend(self):
        #check to ensure that the function returns false when the date is a weekend
        self.assertEqual(c.checkWeekend(self.newBookingTwo[1]), False)
        #check to ensure that the function returns true when the date isnt a weekend
        self.assertEqual(c.checkWeekend(self.newBookingOne[1]), True)

    def test_checkNulls(self):
        #check to make sure no fields are null and returns true
        self.assertEqual(c.checkNulls(self.newBookingOne), True)
        #check to make sure no fields are null and returns false if there are nulls
        self.assertEqual(c.checkNulls(self.newBookingNulls), False)

    def test_checkTimeInAdvance(self):
        #Because of the value of this depending heavily on the current time, the tests must also use the current time
        #This is an edge case that should just fail
        self.assertEqual(c.checkTimeInAdvance((datetime.datetime.now()).strftime('%Y-%m-%d'),(datetime.datetime.now() + datetime.timedelta(hours = 2)).strftime("%H:%M")), False)
        #This is an edge case that should just pass
        self.assertEqual(c.checkTimeInAdvance((datetime.datetime.now()).strftime('%Y-%m-%d'),(datetime.datetime.now() + datetime.timedelta(hours = 4)).strftime("%H:%M")), True)
        #This is a different day and should pass easily
        self.assertEqual(c.checkTimeInAdvance(self.newBookingThree[1],self.newBookingThree[7]), True)

    def test_checkFullMoon(self):
        #check to ensure that the function returns true when the date is a full moon
        self.assertEqual(c.checkFullMoon((self.bookings[1])[0],self.fullMoon), True)
        #check to ensure that the function returns false when the date isnt a full moon
        self.assertEqual(c.checkFullMoon((self.bookings[1])[0],self.Christmas), False)
        #If the room in question is not the moon room this function should always return true
        self.assertEqual(c.checkFullMoon(self.newBookingOne[0],self.Christmas),True)

    def test_checkMaxOcc(self):
         #check to ensure that the function returns true when the room is not at max capacity
         self.assertEqual(c.maxOcc(self.newBookingOne[0], 200), True)
         #check to ensure that the function returns false when the room is at max capacity
         self.assertEqual(c.maxOcc(self.newBookingOne[0], 201), False)
    
    def test_checkAgeRange(self):
        #check to ensure that the function returns true when the age isnt within the range
        rangeF = "0-300"
        self.assertEqual(c.ageRange(self.TestRoom.name, rangeF), False)
        #check to ensure that the function returns false when the age is within the range
        rangeP = "10-30"
        self.assertEqual(c.ageRange(self.TestRoom.name, rangeP), False)
        #check edge case
        rangeE = "0-100"
        self.assertEqual(c.ageRange(self.TestRoom.name, rangeE), False)
    
    def test_getRoom(self):
        #check to ensure that the function returns the correct room
        self.assertEqual(c.getRoom(self.TestFood.name), self.allRooms[2])
        #check that function returns false when the room doesnt exist
        self.assertEqual(c.getRoom("Santa"), False)

    def test_checkDayTimes(self):
        #check to ensure that the function returns times after current time when the time is within the day
        self.assertEqual(c.checkDayTimes(datetime.datetime(2023,7,15, 13, 0,0,0), datetime.date(2023,7,15)), ["14:00", "15:00", "16:00", "17:00", "18:00"])
        #check to make sure all times are returned if the booking is made one day in advance 
        self.assertEqual(c.checkDayTimes(datetime.datetime(2023,7,15), datetime.datetime(2023,7,17)), self.allTimes)
    
    def test_addBooking(self):
        # Set the path to the CSV file
        realFile = "bookings.csv"

        # Set the path to the new copy of the CSV file
        backupFile = "backup.csv"

        # Copy the CSV file
        shutil.copy(realFile, backupFile)
        c.addBooking(self.newBookingOne)
        with open('bookings.csv', mode='r') as file:
            # Create a reader object
            reader = csv.reader(file)
            # Skip the header row (if there is one)
            next(reader, None)
            # Iterate over the rows in reverse order
            for row in reversed(list(reader)):
                # Return the last row
                last_row = row
                break
        shutil.copy(backupFile, realFile)
        test = self.newBookingOne
        for i in range(len(test)):
            test[i] = str(test[i])
        self.assertEqual(self.newBookingOne,last_row)


    def test_form1(self):
        time.sleep(5)
        self.assertEqual((c.form1Checks(self.newBookingOne))[0],True)
        self.assertEqual((c.form1Checks(self.newBookingTwo))[0],False)


    def test_getAvailableTimes(self):
        #check for one hour with a booking
        self.assertEqual(c.getAvabileTimes(datetime.date(2023,4,15), self.TestRoom, "1 hour", self.bookings), ["09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00", "18:00"])
        #check for two hours with a booking
        self.assertEqual(c.getAvabileTimes(datetime.date(2023,4,15), self.TestRoom, "2 hours", self.bookings), ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00"])
        #check for three hours with a booking
        self.assertEqual(c.getAvabileTimes(datetime.date(2023,4,15), self.TestRoom, "3 hours", self.bookings), ["09:00", "10:00"])
        #check for one hour with no booking
        self.assertEqual(c.getAvabileTimes(datetime.date(2023,4,16), self.TestRoom, "1 hour", self.bookings), ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"])
        #check for two hours with no booking
        self.assertEqual(c.getAvabileTimes(datetime.date(2023,4,16), self.TestRoom, "2 hours", self.bookings), ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"])
        #check for three hours with no booking
        self.assertEqual(c.getAvabileTimes(datetime.date(2023,4,16), self.TestRoom, "3 hours", self.bookings), ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"])
    

    #testing csv read/write
    
    
if __name__ == '__main__':
    unittest.main()

