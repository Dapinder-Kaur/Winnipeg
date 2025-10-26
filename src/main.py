import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

check_service = f"https://api.winnipegtransit.com/v2/statuses/schedule.json?api-key={api_key}"
print(check_service)
response  = requests.get(check_service)
res_dir = (response.json())
res_dir_keys = res_dir.keys()
res_dir_status = res_dir['status']
# print(res_dir_status['message'])

nearby_stops = f"https://api.winnipegtransit.com/v2/stops.json?lon=-97.138&lat=49.895&distance=250&api-key={api_key}"
nearby_stop_response = requests.get(nearby_stops)
stops = nearby_stop_response.json()
stops_list = stops['stops']
# print(stops_list[0])


stop_schedule = f"https://api.winnipegtransit.com/v2/stops/10541/schedule.json?max-results-per-route=2&api-key={api_key}"
schedule = requests.get(stop_schedule)
stop_schedule_json = schedule.json()
ss_sc = stop_schedule_json['stop-schedule']
# print(ss_sc['stop']['name'])

# print(ss_sc['route-schedules'][0]['route']['name'])
pretty_print = json.dumps(ss_sc, indent=4)
print(pretty_print)