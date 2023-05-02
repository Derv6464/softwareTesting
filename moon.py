NASAurl = "https://api.nasa.gov/neo/rest/v1/feed"
NASAkey = "KA6ESdqWcKrsNuRgkk2hVtxJAaao9m0daVx0Az0Z"
import datetime
date = datetime.datetime.now()
date = date.date()
import requests
def checkAsteroid():
    response = requests.get(NASAurl, params={"start_date":"2023-01-01","end_date":"2024-01-01","api_key": NASAkey})
    closest_distance = float("inf")
    data = response.json()
    for d in data['near_earth_objects']:
        for asteroid in data['near_earth_objects'][d]:
            closestDate = asteroid['close_approach_data'][0]['close_approach_date']
            print(closestDate)
checkAsteroid()
