# softwareTesting
This is our software testing by Amy McMahon, Dervla Gargan, Mark Langtry.

## Index
- [How to Run](#how-to-run)
- [Project Outline](#project-outline)
- [Results](#results)
- [Contribution](#contribution)


## How to Run
Start with git cloning the repo

To run our website use:
#### Mac
```
$ python3 main.py
```
#### Windows
```
$ python main.py
```
To see the results of our unit tests run this command, this can also been seen through the github actions tab.
### Mac
```
$ python3 tests.py
```
#### Windows
```
$ python tests.py
```
To see the results of our front-end selenuim tests, run this command
#### Mac
```
$ python3 testWeb.py
```
#### Windows
```
$ python testWeb.py
```
You can view the final reports of the coverage and mutation testing [here](#results) or 
view the full results of the coverage report of mutation test through the files in coverage.html/ muatationOut.txt files in the repo or by 

## Project Outline
Our project is a basic room booking system using a simiple HTML website. The goal of this project was to demonstrate our knowledge of testing.
#### Tools used
For our front-end we used the [Pico.css Framework](https://picocss.com/). This kept our front-end simple so we could focus on the main tasks for the project.
For our data stoarge we used a CSV, this contiued to keep things simple.
For our back-end we used Flask as we had all previously used it and were framilar with python.
We used the unittest library for our tests.
We also used Selenium for testing the front-end of our website.

#### Our Website
We used a basic form to book rooms, the user fills out details on what they wanted to book. They are then provided with a list of available times which they can choose from. Once the booking has been made they are shown a confirmation screen.
Different rooms have different conditions to be met so they are able to be booked. 

#### Our Tests
We have two test files. One tests.py has all our unit tests. The second ist testWeb.py, which uses selenium to test the front end of our website.

#### Our Extras
We used GitHub actions to automate our tests. We also used at .env to store our API keys. This was also autmomated through GitHub Actions. We used a linter to format our code. We also did mutation testing and used a coverage report.


## Results
coverage and mutation here 

## Contribution
Percentage is in the order of names in contributions

Note: The is a broad overveiw as the amount of time and complexity differ for each function, file or task.
#### HTML
|File Name|Contributions|Percentage|
|---------|-------------|----------|
|home.html|Amy McMahon|100%|
|selectTime.html|Amy McMahon|100%|
|details.html|Amy McMahon|100%|
|confirm.html|Dervla Gargan|100%|
| | | |
|Overall|Amy McMahon,Dervla Gargan|75%,25%|

### constaints.py
|Function Name|Contributions|Percentage|
|---------|-------------|----------|
|getBookings()|Dervla Gargan|100%|
|form1Checks()|Dervla Gargan,Amy McMahon|60%,40%|
|form2Checks()|Dervla Gargan|100%|
|getRoom()|Dervla Gargan,Mark Langtry|50%,50%|
|ageRange()|Amy McMahon,Mark Langtry|80%,20%|
|maxOcc()|Amy McMahon,Mark Langtry|90%,10%|
|checkDayTimes()|Dervla Gargan|100%|
|getAvabileTimes()|Dervla Gargan,Amy McMahon|80%,20%|
|addBooking()|Dervla Gargan|100%|
|userBooked()|Dervla Gargan|100%|
|checkWeekend()|Mark Langtry|100%|
|checkTimeInAdvance()|Dervla Gargan,Mark Langtry|60%,40%|
|checkHoliday()|Mark Langtry|100%|
|checkFullMoon()|Mark Langtry|100%|
| | | |
|Overall|Amy McMahon,Dervla Gargan,Mark Langtry|16%,53%,30%|


### main.py
|Function Name|Contributions|Percentage|
|---------|-------------|----------|
|home()|Amy McMahon|100%|
|onSubmit()|Amy McMahon,Dervla Gargan|50%,50%|
|onTimeSubmit()|Amy McMahon,Dervla Gargan|40%,60%|
|roomDetails()|Amy McMahon|100%|
|backHome()|Amy McMahon|100%|
| | | |
|Overall|Amy McMahon,Dervla Gargan|78%,22%|
### tests.py
|Function Name|Contributions|Percentage|
|---------|-------------|----------|
|setUp()|Amy McMahon,Mark Langtry|50%,50%|
|test_checkHoliday()|Amy McMahon,Mark Langtry|50%,50%|
|test_userBooked()|Amy McMahon|100%|
|test_checkWeekend()|Amy McMahon,Mark Langtry|50%,50%|
|test_checkTimeInAdvance()|Mark Langtry|100%|
|test_checkFullMoon()|Mark Langtry,Amy McMahon|66%,34%|
|test_checkMaxOcc()|Amy McMahon|100%|
|test_checkAgeRange()|Amy McMahon,Mark Langtry|70%,30% |
|test_getRoom()|Amy McMahon|100%|
|test_checkDayTime()|Amy McMahon|100%|
|test_addBooking()|Mark Langtry|100%|
|test_form1()|Mark Langtry|100%|
|test_form2()|Amy McMahon|100%|
|test_getAvailableTimes()|Amy McMahon|100%|
||||
|Overall|Amy McMahon,Mark Langtry|61%,39%|

### Extras
|Name|Contributions|Percentage|
|---------|-------------|----------|
|testWeb.py (selenium)|Dervla Gargan|100%|
|Linting|Amy McMahon|100%|
|Github Actions|Amy McMahon,Dervla Gargan|50%,50%|
|.env/secrets key|Amy McMahon,Dervla Gargan|50%,50%|
|coverage|Amy McMahon|100%|
|mutation|Mark Langtry,Dervla Gargan|80%,20%|
|Read Me|Amy McMahon,Dervla Gargan,Mark Langtry|10%,80%,10%|
||||
|Overall|Amy McMahon,Dervla Gargan,Mark Langtry|44%,43%,13%|
