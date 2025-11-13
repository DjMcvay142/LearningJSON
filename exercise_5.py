#Exercise 5 - Making JSON Readable

import json

try:
    with open("exercise5.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
        data = {
            "user142": {
                "name": "Dan",
                "command_used": 5
            },
            "user420": {
                "name": "Deri",
                "command_used": 2
            },
            "user6767": {
                "name": "Tobias",
                "command_used": 0
            }
        }

data["user6767"]["command_used"] += 1
with open("exercise5.json", "w") as file:
    json.dump(data, file, indent=4, sort_keys=True)

print(data)