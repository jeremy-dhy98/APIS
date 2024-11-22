import requests as re
import json
import os
API_KEY = os.environ.get("CAT_API_KEY")

url = "https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key=API_KEY" #Api basic info -->call base url
response =  re.get(url)
code = response.status_code
print(response.status_code)
print(response.reason)
if response:
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    jprint(response.json())
else:
    raise Exception(f"Non-success status code", response.status_code,response.reason)
    
print(response.text)
print("Headers: ",response.headers )# Check contents of the response / what info an api contains
print("Method: ", response.request)
req = response.request
print("URL: ",req.url,"\nPath url: ",req.path_url, "\nHeaders: ",req.headers)
print(response.reason)#Know why you are getting certin response code

#Providing endpoints to an API
#This enables you to querry some specific information
#To include more than one endpoint use & eg-->/images/search?limit=10$breed_ids="id"$api_key=API_KEY
