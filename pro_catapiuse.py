import requests
import json
import os
from requests.exceptions import HTTPError

API_KEY = os.environ.get("CAT_API_KEY")
url = "https://api.thecatapi.com/v1/images/search/"
payload = {"format":"json","has_breeds":1,"breed_ids":"beng",
           "limit":10,"page":7,"order":"ASC"}
headers = {"x-api-key":"API_KEY"}

try:
    def getcats():
        response = requests.get(url, params=payload, headers=headers)
        response.raise_for_status()
        return response
except HTTPError as HTTPerr:
    print(f"an HTTPError occured: {HTTPerr}")
except Exception as err:
    print(f"Other type of error occured: {err}")
else:
    print("Querry success.")

r = getcats()
def jprint(obj):
    text = json.dumps(obj,sort_keys=True, indent=4)
    return text
dict = jprint(r.json())
# print(dict)
