import csv
import unittest
from unittest import mock
from datetime import datetime, timedelta, date
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import constaints as c



class TestStringMethods(unittest.TestCase):
    # Setup for testing
    def setUp(self):
        self.Christmas = datetime(2023, 12, 25)
        self.fullMoon = datetime(2023, 3, 7)
        # self.Christmas = '2023-12-25'
        # self.fullMoon = '2023-3-7'
        # name, phone, date, time, bookings
        self.TestRoom = c.Room("Meeting", 6, 100, 0)
        self.TestFood = c.Room("Food", 15, 100, 1)
        self.TestMoonRoom = c.Room("Moon", 6, 100, 0)
        self.allRooms = c.allRooms
        self.allTimes = c.allTimes
        self.bookings = [
            [
                self.TestRoom,
                date(2023, 4, 15),
                11,
                "1 hours",
                44,
                "John",
                "0123456789",
                "13:00",
            ],
            [
                self.TestMoonRoom,
                date(2023, 4, 16),
                7,
                "2 hours",
                30,
                "Jane",
                "9876543210",
                "14:00",
            ],
            [
                self.TestRoom,
                date(2023, 4, 17),
                22,
                "1 hours",
                60,
                "Bob",
                "0123456789",
                "15:00",
            ],
        ]
        self.newBookingForm = [
            self.TestRoom,
            date(2023, 4, 17),
            100,
            "1 hours",
            "20-40",
            "Jane",
            "9876543210",
            "14:00",
        ]
        self.newBookingForm2 = [
            self.TestMoonRoom,
            date(2023, 4, 17),
            100,
            "1 hours",
            "20-40",
            "Jane",
            "9876543210",
            "14:00",
        ]
        self.newBookingOne = [
            self.TestRoom,
            date(2023, 4, 16),
            100,
            "1 hours",
            40,
            "Jane",
            "9876543210",
            "14:00",
        ]
        self.newBookingTwo = [
            self.TestRoom,
            date(2023, 4, 17),
            60,
            "1 hours",
            40,
            "Bob",
            "9876543210",
            "14:00",
        ]
        self.newBookingThree = [
            self.TestRoom,
            date(2023, 6, 17),
            60,
            "1 hours",
            40,
            "Bob",
            "9876543210",
            "14:00",
        ]
        self.newBookingNulls = [
            "",
            date(2023, 4, 17),
            25,
            "1 hours",
            40,
            "Bob",
            "9876543210",
            "14:00",
        ]
        self.newBookingMax = [
            self.TestFood,
            date(2023, 4, 17),
            60,
            "1 hours",
            40,
            "Sarah",
            "9876543210",
            "14:00",
        ]

    # api testing
    def test_checkHoliday(self):
        # check to ensure that the function returns false when the date is a holiday
        self.assertEqual(c.checkHoliday(self.Christmas), False)
        time.sleep(5)
        # check to ensure that the function returns true when the date isn't a holiday
        self.assertEqual(c.checkHoliday(self.newBookingForm[1]), True)

    def test_userBooked(self):
        # check to ensure that the function returns False when the user already has a booking
        self.assertEqual(
            c.userBooked(
                self.newBookingOne[5],
                self.newBookingOne[6],
                self.newBookingOne[1],
                self.newBookingOne[7],
                self.bookings,
            ),
            False,
        )
        # check to ensure that the function returns true when the user doesnt already have a booking
        self.assertEqual(
            c.userBooked(
                self.newBookingTwo[5],
                self.newBookingTwo[6],
                self.newBookingTwo[1],
                self.newBookingTwo[7],
                self.bookings,
            ),
            True,
        )

    def test_checkWeekend(self):
        # check to ensure that the function returns false when the date is a weekend
        self.assertEqual(c.checkWeekend(self.newBookingOne[1]), False)
        # check to ensure that the function returns true when the date isnt a weekend
        self.assertEqual(c.checkWeekend(self.newBookingTwo[1]), True)

    def test_checkNulls(self):
        # check to make sure no fields are null and returns true
        self.assertEqual(c.checkNulls(self.newBookingOne), True)
        # check to make sure no fields are null and returns false if there are nulls
        self.assertEqual(c.checkNulls(self.newBookingNulls), False)

    def test_checkTimeInAdvance(self):
        # Because of the value of this depending heavily on the current time, the tests must also use the current time
        # This is an edge case that should just fail
        d = datetime(2022, 12, 28, 16, 55, 59)
        if datetime.now().hour < 22:
            self.assertEqual(
                c.checkTimeInAdvance(
                    d,
                    d.date(),
                    (d + timedelta(hours=2)).strftime("%H:%M"),
                ),
                False,
            )
        # This is an edge case that should just pass
        if datetime.now().hour < 20:
            self.assertEqual(
                c.checkTimeInAdvance(
                    d,
                    d.date(),
                    (d + timedelta(hours=4)).strftime("%H:%M"),
                ),
                True,
            )
        # This is a different day and should pass easily
        self.assertEqual(
            c.checkTimeInAdvance(
                d, self.newBookingThree[1], self.newBookingThree[7]
            ),
            True,
        )

    def test_checkFullMoon(self):
        # check to ensure that the function returns true when the date is a full moon
        self.assertEqual(c.checkFullMoon((self.bookings[1])[0], self.fullMoon), True)
        # check to ensure that the function returns false when the date isnt a full moon
        self.assertEqual(c.checkFullMoon((self.bookings[1])[0], self.Christmas), False)
        # If the room in question is not the moon room this function should always return true
        self.assertEqual(c.checkFullMoon(self.newBookingOne[0], self.Christmas), True)

    def test_checkMaxOcc(self):
        # check to ensure that the function returns true when the room is not at max capacity
        self.assertEqual(c.maxOcc(self.newBookingOne[0], 200), True)
        # check to ensure that the function returns false when the room is at max capacity
        self.assertEqual(c.maxOcc(self.newBookingOne[0], 201), False)

    def test_checkAgeRange(self):
        # check to ensure that the function returns true when the age isnt within the range
        rangeF = "0-300"
        self.assertEqual(c.ageRange(self.TestRoom, rangeF), False)
        # check to ensure that the function returns false when the age is within the range
        rangeP = "10-30"
        self.assertEqual(c.ageRange(self.TestRoom, rangeP), False)
        # check edge case
        rangeE = "0-100"
        self.assertEqual(c.ageRange(self.TestRoom, rangeE), False)

    def test_getRoom(self):
        # check to ensure that the function returns the correct room
        self.assertEqual(c.getRoom(self.TestFood.name), self.allRooms[2])
        # check that function returns false when the room doesnt exist
        self.assertEqual(c.getRoom("Santa"), False)

    def test_checkDayTimes(self):
        # check to ensure that the function returns times after current time when the time is within the day
        self.assertEqual(
            c.checkDayTimes(datetime(2023, 7, 15, 13, 0, 0, 0), date(2023, 7, 15)),
            ["14:00", "15:00", "16:00", "17:00", "18:00"],
        )
        # check to make sure all times are returned if the booking is made one day in advance
        self.assertEqual(
            c.checkDayTimes(datetime(2023, 7, 15), datetime(2023, 7, 17)), self.allTimes
        )

    def test_addBooking(self):
        # Set the path to the CSV file
        realFile = "bookings.csv"

        # Set the path to the new copy of the CSV file
        backupFile = "backup.csv"

        # Copy the CSV file
        shutil.copy(realFile, backupFile)
        c.addBooking(self.newBookingOne)
        with open("bookings.csv", mode="r") as file:
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
        # making types match the types in the room class
        last_row[0] = c.getRoom(last_row[0])
        last_row[1] = datetime.strptime(last_row[1], "%Y-%m-%d").date()
        last_row[2] = int(last_row[2])
        last_row[4] = int(last_row[4])
        # seperate check for names as cant compare objects
        self.assertEqual(self.newBookingOne[0].name, last_row[0].name)
        # comparing rest of the values
        self.assertEqual(self.newBookingOne[1:], last_row[1:])

    def test_form1(self):
        time.sleep(5)
        self.assertEqual((c.form1Checks(self.newBookingForm))[0], True)
        # self.assertEqual((c.form1Checks(self.newBookingTwo))[0],False)

    def test_form2(self):
        self.assertEqual((c.form2Checks(self.newBookingForm))[0], True)

    def test_getAvailableTimes(self):
        # check for one hour with a booking
        self.assertEqual(
            c.getAvabileTimes(
                date(2023, 4, 15), self.TestRoom, "1 hour", self.bookings
            ),
            [
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "14:00",
                "15:00",
                "16:00",
                "17:00",
                "18:00",
            ],
        )
        # check for two hours with a booking
        self.assertEqual(
            c.getAvabileTimes(
                date(2023, 4, 15), self.TestRoom, "2 hours", self.bookings
            ),
            ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00"],
        )
        # check for three hours with a booking
        self.assertEqual(
            c.getAvabileTimes(
                date(2023, 4, 15), self.TestRoom, "3 hours", self.bookings
            ),
            ["09:00", "10:00", "14:00", "15:00", "16:00"],
        )
        # check for one hour with no booking
        self.assertEqual(
            c.getAvabileTimes(date(2023, 4, 1), self.TestRoom, "1 hour", self.bookings),
            [
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
            ],
        )
        # check for two hours with no booking
        self.assertEqual(
            c.getAvabileTimes(
                date(2023, 4, 18), self.TestRoom, "2 hours", self.bookings
            ),
            [
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
                "17:00",
            ],
        )
        # check for three hours with no booking
        self.assertEqual(
            c.getAvabileTimes(
                date(2023, 4, 18), self.TestRoom, "3 hours", self.bookings
            ),
            ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"],
        )

    # testing csv read/write


if __name__ == "__main__":
    unittest.main()
