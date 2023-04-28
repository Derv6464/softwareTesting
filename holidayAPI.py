import requests

url = "https://holidays.abstractapi.com/v1/"
api_key = "f9eb73a590b245259d9ecf7b8717445b"


country = "IE"
day = 25
month = 12
year = 2023


response = requests.get(url, params={"api_key": api_key, "country": country, "year": year, "month": month, "day": day})

print(response.content)