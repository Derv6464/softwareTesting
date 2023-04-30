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
        self.TestRoom = c.Room("meeting",6,100,0)
        self.bookings = [
            ["Meeting", '2023-04-15', 11, "1 hour", 44, 'John', '0123456789', '13:00'],
            ["Moon", '2023-04-16', 7, "2 hours", 30, 'Jane', '9876543210', '14:00'],
            ["Meeting", '2023-04-17',22, "1 hour", 60, 'Bob', '0123456789', '15:00']
        ]
        self.newBookingOne = ["Meeting", '2023-04-16', 100, "1 hour", 40, 'Jane', '9876543210', '14:00']
        self.newBookingTwo = ["Meeting", '2023-04-17', 100, "1 hour", 40, 'Bob', '9876543210', '14:00']
        self.newBookingNulls = ["", '2023-04-17', 100, "1 hour", 40, 'Bob', '9876543210', '14:00']
    
    #api testing
    def test_checkHoliday(self):
        #check to ensure that the function returns true when the date is a holiday
        self.assertEqual(c.checkHoliday(self.Christmas), False)

    def test_userBooked(self):
        #check to ensure that the function returns False when the user already has a booking
        self.assertEqual(c.userBooked(self.newBookingOne[5], self.newBookingOne[6], self.newBookingOne[1], self.newBookingOne[7], self.bookings),False)

    def test_userNotBooked(self):
        #check to ensure that the function returns true when the user doesnt already have a booking
        self.assertEqual(c.userBooked(self.newBookingTwo[5], self.newBookingTwo[6], self.newBookingTwo[1], self.newBookingTwo[7], self.bookings),True)

    def test_checkWeekend(self):
        #check to ensure that the function returns true when the date is a weekend
        self.assertEqual(c.checkWeekend(datetime.datetime(2023,4,28)), True)

    def test_checkNulls(self):
        #check to make sure no fields are null and returns true
        self.assertEqual(c.checkNulls(self.newBookingOne), True)
        #check to make sure no fields are null and returns false if there are nulls
        self.assertEqual(c.checkNulls(self.newBookingNulls), False)

    # def test_checkTimeInAdvance(self):
    #    self.assertEqual(c.checkTimeInAdvance("13:00", self.newBookingOne[7]), True)

    def test_checkFullMoon(self):
        #check to ensure that the function returns true when the date is a full moon
        self.assertEqual(c.checkFullMoon(self.fullMoon), True)
        #check to ensure that the function returns false when the date isnt a full moon
        self.assertEqual(c.checkFullMoon(self.Christmas), False)

    #testing front end
        

    #def test_search_in_python_org(self):
    #    options = Options()
    #    options.headless = True
    #    self.driver = webdriver.Chrome('./chromedriver', options=options)
    #    driver = self.driver
    #    driver.get("http://127.0.0.1:5000")
    #    print(driver.title)
    #    self.assertEqual("Bookings", driver.title)
    #    self.driver.close()
       

    #testing csv read/write
    
    
if __name__ == '__main__':
    unittest.main()


