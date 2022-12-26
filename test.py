import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes": 10, "name": "semion","views":100000})
print(response.json())
