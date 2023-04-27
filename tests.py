import unittest
import datetime
import constaints as c
class TestStringMethods(unittest.TestCase):
    Christmas = datetime.datetime(2023,12,25)
    Tester = c.User(True, 1234, 6, Christmas)
    TestRoom = c.Room("meeting",6)
    def test_checkHoliday(Tester):
        Tester.assertEqual(c.checkHoliday(Tester.date), False)
    def test_checkValidId(Tester):
        Tester.assertEqual(c.checkValidId(Tester.id), True)
    def test_userBooked(Tester):
        Tester.assertEqual(c.userBooked(Tester.booking),False)
    def test_checkWeekend(Tester):
        Tester.assertEqual(c.checkWeekend(Tester.date), True)
    def test_checkTimeInAdvance(Tester):
        Tester.assertEqual(c.checkTimeInAdvance(Tester.date), True)
if __name__ == '__main__':
    unittest.main()

