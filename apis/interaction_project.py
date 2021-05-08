import requests
from pprint import pprint

response = requests.get("https://swapi.dev/api/starships/9/")

pprint(response.json())

data = response.json()

print("name :", data["name"])
print("model :", data["model"])
print("crew :", data["crew"])
print("length :", data["length"])