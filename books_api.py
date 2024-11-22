import json
import requests
import os

# API_KEY = "AIzaSyCIAcNBkPcICXCtB0-8xzfElj3YqRMZDzQ"
# print(API_KEY)
url = "https://openlibrary.org/api/books?bibkeys=ISBN:0375701621&format=json"
response = requests.get(url)
if response:
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    jprint(response.json())
else:
    raise Exception(f"Non-success status code", response.status_code,response.reason)
