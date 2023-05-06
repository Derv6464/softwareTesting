import datetime
import os
from dotenv import load_dotenv
import requests
url = "https://holidays.abstractapi.com/v1/"

def checkHoliday(date):
    load_dotenv()
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    country = "IE"
    day = date.day
    month = date.month
    year = date.year
    response = requests.get(url, params={"api_key": os.getenv("HOLIDAY_API"), "country": country, "year": year, "month": month, "day": day})
    print(response.text)
    #if response.status_code!=200:
    #    return True
    if response.text == "[]": 
        return True
    else:
        return False
    
print(checkHoliday("2023-12-25"))