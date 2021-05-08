# pip install requests

import requests

from pprint import pprint

response = requests.get("https://swapi.dev/api/people/1")

pprint(response.json())

data = response.json()

print("eye color :", data["eye_color"])
print("eye color :", data["name"])
print("hair color :", data["hair_color"])

# sends a GET request and store the response as response
response = requests.get("https://swapi.dev/api/people")
pprint(response.json())

# response.json() converts the response to a dictionary
data = response.json()

# people is a list at the key results in the data dictonary
people = data["results"]

# we can iterate over a list from the sjon
# and print useful information
for person in people:
    print("name :", person["name"])
    print("eye color", person["eye_color"])

    for starship in person["starships"]:
        print("starship url", starship)