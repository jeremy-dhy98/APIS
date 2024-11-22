#HTTP Headers define info abt the response.
#This includes:
"""-Accept(what type of content the client accepts
   -Content type(What kind of info the server should respond with)
   -User_Agent(What s/w the client is using to connect with the server)
   -Server(s/w the server using to comm. with the client)
   -Authentication(Who's calling the api and what credentials they have-->api_keys etc)
"""
#Custom headers are used to request or send additinal info from clients.They usually start with X-
#Headers are defined in a dict and send along with your request using the "headers=" param of the .get()
import requests
from requests.exceptions import HTTPError

url = "https://api.github.com/search/repositories"
params = {"q":"language:python","sort":"stars","order":"desc","limit":4} #or b"q:language:python&sort:stars&order:desc"(params as bytes)
headers = {}
try:
    result = requests.get(url,params=params)
    result.raise_for_status()
except HTTPError as err:
    print(f"HTTP Error Occured: {err}")
except Exception as err:
    print(f"Other Error occured: {err}")
else:
    print("Querry success!")
    print(result.json())
