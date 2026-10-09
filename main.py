import argparse
import json
from pathlib import Path
from datetime import datetime

# --- loads data from data.json into a list of dicts. each dict is a task, and contains all info related to said task. --- #
def fetch_data() -> list:
    try:
        with open("data.json", "r") as file:
            return json.load(file)

# --- ensures that the index of the task in the list "data" is the same as the "id" in the list of dicts. --- #
def calibrate_indicies(index:int, data: list):
    while index != data[index]["id"]: 
        if index < data[index]["id"]:
            index += 1
        else:
            index -= 1

def add_task(desc: str):
    data = fetch_data()

    new_task = {"id" : len(data), "desc" : desc, "status" : "todo", "createdAt" : datetime.now(), "updatedAt" : None}
    data.append(new_task)

    print(f"New task {desc} officially created at {new_task["createdAt"]}")
    
    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)


def update_task(task_id:int, new_desc=None, new_status=None):
    data = fetch_data()
    calibrate_indicies(task_id, data)
    
    data[task_id]["updatedAt"] = datetime.now()

    if new_desc:
        data[task_id]["desc"] = new_desc
    if new_status:
        data[task_id]["status"] = new_status

def delete_task(task_id: int):
    data = fetch_data()
    calibrate_indices(task_id, data)

    data.remove(task_id)

    # --- updates each id to exist within 0 to n, with n being the 1 minus the length of the list holding each task (dict) --- #
    i = 0
    while i < len(data):
        if i != data[i]["id"]:
            data[i]["id"] = i
        i += 1

def list_tasks():
    # TODO list all tasks

    data = fetch_data()

    for task in data:
        print(f"ID: {task["id"]} Description: {task["desc"]} Status: {task["status"]} Created at: {task["createdAt"]} Updated at: {task["updatedAt"]}")
    
def list_tasks_done():
    for task in data:
        if task["status"] == "done":
            print(f"ID: {task["id"]} Description: {task["desc"]} Status: {task["status"]} Created at: {task["createdAt"]} Updated at: {task["updatedAt"]}")
    
def list_tasks_todo():
    for task in data:
        if task["status"] == "todo":
            print(f"ID: {task["id"]} Description: {task["desc"]} Status: {task["status"]} Created at: {task["createdAt"]} Updated at: {task["updatedAt"]}")

def list_tasks_in_progress():
    for task in data:
        if task["status"] == r"in-progress":
            print(f"ID: {task["id"]} Description: {task["desc"]} Status: {task["status"]} Created at: {task["createdAt"]} Updated at: {task["updatedAt"]}")





def main():
    parser = argparse.ArgumentParser(prog="tasktracker", description="A simple CLI task tracking tool.", epilog="Made by Alex Furst.")

    parser.add_argument("action", type=str, choices=["add","delete","update","list","list_done","list_todo","list_in_progress"] help="Add a task to the task tracker")



