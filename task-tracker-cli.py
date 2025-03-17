#check for the json file is exist if not create empy json file
import os
import json

file_name = "list.json"

if not os.path.exists(file_name):
    with open(file_name, "w") as file:
        json.dump({},file)
        print(f"{file_name} was created.")
else:
    print(f"{file_name} already exists")
