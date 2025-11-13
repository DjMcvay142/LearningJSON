#Exercise 2 - JSON File Basics

import json

user_data = {
    "firstName": "Dan",
    "lastName": "McVay",
    "university": "Northumbria University",
    "course": "Computing and Information Science"
}


with open("user.json", "w") as file:
    json.dump(user_data, file)

with open("user.json", "r") as file:
    data = json.load(file)
    print(data)
    print(f"Their first name is {data["firstName"]}")
    data["academicYear"] = "Foundation Year"

with open("user.json", "w") as file:
    json.dump(data, file)

with open("user.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)