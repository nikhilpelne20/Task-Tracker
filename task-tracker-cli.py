import os
import json
import argparse
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
        "progress": "todo",
        "CreatedDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    tasks.append(new_task)
    save_task(tasks)
    print(f"Task added successfully: {new_task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No Task found!")
        return
    print("All Tasks:")
    for task in tasks:
        print(f"[{task['id']}] {task['task']} - {task['progress']}")



def update_task(task_id, updated_task):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = updated_task
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_task(tasks)
            print("Task updated successfully")
            return
    print(f"Task with ID {task_id} not Found.")




def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['progress'] = "in-progress"
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_task(tasks)
            print("Task marked in-progress successfully")
            return
    print(f"Task with ID {task_id} not Found.")



def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['progress'] = "done"
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_task(tasks)
            print("Task marked done successfully")
            return 
    print(f"Task with ID {task_id} not Found.")



def mark_todo(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['progress'] = "todo"
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_task(tasks)
            print("Task marked done successfully")
            return 
    print(f"Task with ID {task_id} not Found.")



def list_task_status(status):
    tasks = load_tasks()
    filtered_task = [task for task in tasks if task["progress"] == status]
    if not filtered_task:
        print(f"no task with status: {status} found")
        return
    print(f"task with status: {status} :")
    for task in filtered_task:
        print(f"[{task['id']}] {task['task']}")


def main():




