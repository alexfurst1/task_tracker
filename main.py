import argparse
import json
from pathlib import Path
from datetime import datetime

def fetch_data() -> list:
    try:
        with open("data.json", "r") as file:
            return json.load(file)

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

    while task_id != data[task_id]["id"]:
        if task_id < data[task_id]["id"]:
            task_id += 1
        else:
            task_id -= 1
    
    data[task_id]["updatedAt"] = datetime.now()

    if new_desc:
        data[task_id]["desc"] = new_desc
    if new_status:
        data[task_id]["status"] = new_status

def delete_task(task_id: int):

    data = fetch_data()

    while task_id != data[task_id]["id"]:
        if task_id < data[task_id]["id"]:
            task_id += 1
        else:
            task_id -= 1

    data.remove(task_id)

    i = 0
    while i < len(data):
        if i != data[i]["id"]:
            data[i]["id"] = i
        i += 1

def list_tasks():
    # TODO list all tasks
    
def list_tasks_complete():
    
def list_tasks_incomplete():

def list_tasks_in_progress():






def main():
    parser = argparse.ArgumentParser(description="A simple CLI task tracking tool.")



