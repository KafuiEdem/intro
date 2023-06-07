"""
    1. Using requests connect to https://jsonplaceholder.typicode.com/users and take the JSON encoded string in Python object

    2. The resulting Python object will be a list of dictionaries. Process the list and extract the following information for each user:

    - Name

    - City

    - GPS coordinates in form of (LAT, LNG)

    - Company's name the user is working for

    3. Write to a CSV File a row for each user. The fields of the CSV file will be: name, city, GPS coordinates and company's name

""" 
import requests
import json
import csv

URL = "https://jsonplaceholder.typicode.com/users"

respons = requests.get(URL)

data = json.loads(respons.text)
with open("user_list.csv","w") as f:
   csv_file = csv.writer(f)
   csv_file.writerow(["name", "city", "GPS coordinates","company's name"])
   for names in data:
        name = names["name"]
        city = names["address"]["city"]
        lat = names["address"]["geo"]["lat"]
        lng = names["address"]["geo"]["lng"]
        company = names["company"]["name"]

        csv_file.writerow([name,city,f"lat:{lat},lng{lng}",company])
    
