#check for the json file is exist if not create empy json file
import os
import json

file_name = "list.json"

if not os.path.exists(file_name):
    with open(file_name, "w") as file:
        json.dump([],file, indent=4)
        print(f"{file_name} was created.")

def load_tasks():
    with open(file_name, "r") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []

task = load_tasks()
print(task)
