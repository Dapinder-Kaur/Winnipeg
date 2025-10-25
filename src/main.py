import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("API_KEY")

check_service = f"https://api.winnipegtransit.com/v2/statuses/schedule.json?api-key={api_key}"
print(check_service)

response  = requests.get(check_service)

res_dir = (response.json())

res_dir_keys = res_dir.keys()
# print(f"API Key: {api_key}")

res_dir_status = res_dir['status']

print(res_dir_status['message'])