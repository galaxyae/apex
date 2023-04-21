import json

locations = []

map = {}

f = open('cities.json',)
cities = json.load(f)
for i in locations:
    for j in cities:
        print(j['name'].lower())
