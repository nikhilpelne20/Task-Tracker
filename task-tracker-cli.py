import os
import json
from datetime import datetime

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

def save_task(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks,file, indent= 4)


def add_task(task):
    tasks = load_tasks()

    new_id = tasks[-1]["id"] + 1 if tasks else 1

    new_task = {
        "id": new_id,
        "task": task,
        "progress": "to-do",
        "CreatedDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    tasks.append(new_task)
    save_task(tasks)
    print(f"Task added successfully: {new_task}")

def list_tasks():
    tasks = load_tasks()
    task_list = []
    for task in tasks:
        task_list.append(task['task'])
    return task_list






# add_task("Complete Python project")
# add_task("Learn JavaScript")
