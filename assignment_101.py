import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"

r = requests.get(url=url)

raw_json = r.json()

for i in raw_json:
    if i["completed"]==True:
        print(i)
