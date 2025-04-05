import json


with open("tasks.json",'r') as file:
    tasks = json.load(file)
    print(tasks[1]["done"])