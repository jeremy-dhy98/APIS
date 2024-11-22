import requests

url = "https://bible_api.com/ 3: 16"
result = requests.get(url)
result.status_code
print(result.reason)
print(result.json())