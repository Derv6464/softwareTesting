import unittest
import datetime
import time
import constaints as c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TestStringMethods(unittest.TestCase):

    #api testing
    Christmas = datetime.datetime(2023,12,25)
    Tester = c.User(True, 1234, 6, Christmas)
    TestRoom = c.Room("meeting",6,100,0)
    def test_checkHoliday(self):
        self.assertEqual(c.checkHoliday(datetime.datetime(2023,12,25)), False)

    #testing constaints
    #def test_checkValidId(self,Tester):
    #    self.assertEqual(c.checkValidId(Tester.id), True)
    #def test_userBooked(self,Tester):
    #    self.assertEqual(c.userBooked(Tester.booking),False)
    def test_checkWeekend(self):
        self.assertEqual(c.checkWeekend(datetime.datetime(2023,4,28)), True)
    #def test_checkTimeInAdvance(self):
    #   self.assertEqual(c.checkTimeInAdvance(Tester.date), True)

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

