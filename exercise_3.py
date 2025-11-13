#Exercise Three: Handling files that don't exist

import json

try:
    with open("exercise3.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    with open("exercise3.json", "w") as file:
        data = {}
        json.dump(data, file)

print(data)

