import unittest
import datetime
import time
import constaints as c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TestStringMethods(unittest.TestCase):

    #Setup for testing
    def setUp(self):
        self.Christmas = datetime.datetime(2023,12,25)
        self.fullMoon = datetime.datetime(2023,3,7)
        #name, phone, date, time, bookings
        self.Tester = c.User(True, 10, 10, self.Christmas)
        self.TestRoom = c.Room("Meeting",6,100,0)
        self.TestMoonRoom = c.Room("Moon",6,100,0)
        self.bookings = [
            ["Meeting", '2023-04-15', 11, "1 hour", 44, 'John', '0123456789', '13:00'],
            ["Moon", '2023-04-16', 7, "2 hours", 30, 'Jane', '9876543210', '14:00'],
            ["Meeting", '2023-04-17',22, "1 hour", 60, 'Bob', '0123456789', '15:00']
        ]
        self.newBookingOne = ["Meeting", '2023-04-16', 100, "1 hour", 40, 'Jane', '9876543210', '14:00']
        self.newBookingTwo = ["Meeting", '2023-04-17', 60, "1 hour", 40, 'Bob', '9876543210', '14:00']
        self.newBookingNulls = ["", '2023-04-17', 25, "1 hour", 40, 'Bob', '9876543210', '14:00']
        self.newBookingMax = ["Food", '2023-04-17', 60, "1 hour", 40, 'Sarah', '9876543210', '14:00']
    
    #api testing
    def test_checkHoliday(self):
        # check to ensure that the function returns false when the date is a holiday
        self.assertEqual(c.checkHoliday(self.Christmas), False)
        # check to ensure that the function returns true when the date isn't a holiday
        self.assertEqual(c.checkHoliday(datetime.datetime(2023, 4, 30)), True)

    def test_userBooked(self):
        #check to ensure that the function returns False when the user already has a booking
        self.assertEqual(c.userBooked(self.newBookingOne[5], self.newBookingOne[6], datetime.datetime.strptime(self.newBookingOne[1], "%Y-%m-%d"), self.newBookingOne[7], self.bookings),False)
        #check to ensure that the function returns true when the user doesnt already have a booking
        self.assertEqual(c.userBooked(self.newBookingTwo[5], self.newBookingTwo[6], datetime.datetime.strptime(self.newBookingTwo[1], "%Y-%m-%d"), self.newBookingTwo[7], self.bookings),True)
 

    def test_checkWeekend(self):
        #check to ensure that the function returns false when the date is a weekend
        self.assertEqual(c.checkWeekend(datetime.datetime(2023,4,29)), False)
        #check to ensure that the function returns true when the date isnt a weekend
        self.assertEqual(c.checkWeekend(datetime.datetime(2023,4,25)), True)

    def test_checkNulls(self):
        #check to make sure no fields are null and returns true
        self.assertEqual(c.checkNulls(self.newBookingOne), True)
        #check to make sure no fields are null and returns false if there are nulls
        self.assertEqual(c.checkNulls(self.newBookingNulls), False)

    # def test_checkTimeInAdvance(self):
    #    self.assertEqual(c.checkTimeInAdvance("13:00", self.newBookingOne[7]), True)

    def test_checkFullMoon(self):
        #check to ensure that the function returns true when the date is a full moon
        self.assertEqual(c.checkFullMoon(self.TestMoonRoom,self.fullMoon), True)
        #check to ensure that the function returns false when the date isnt a full moon
        self.assertEqual(c.checkFullMoon(self.TestMoonRoom,self.Christmas), False)

    def test_checkMaxOcc(self):
         #check to ensure that the function returns true when the room is not at max capacity
         self.assertEqual(c.maxOcc(self.TestRoom, 4), True)
         #check to ensure that the function returns false when the room is at max capacity
         self.assertEqual(c.maxOcc(self.TestRoom, 8), False)
    
    def test_checkAgeRange(self):
        #check to ensure that the function returns true when the age isnt within the range
        rangeF = "0-300"
        self.assertEqual(c.ageRange(self.TestRoom, rangeF), True)
        #check to ensure that the function returns false when the age is within the range
        rangeP = "10-30"
        self.assertEqual(c.ageRange(self.TestRoom, rangeP), False)
        #check edge case
        rangeE = "0-100"
        self.assertEqual(c.ageRange(self.TestRoom, rangeE), False)

        
    
       

    #testing csv read/write
    
    
if __name__ == '__main__':
    unittest.main()

