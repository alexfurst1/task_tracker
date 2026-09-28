import argparse
from pathlib import Path

def create_id():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)


class Task:
    def __init__(desc: str):
        self.id = 
        self.desc = desc



def add_task(id, desc, status, createdAt, updatedAt):
    # TODO add a new task to the list
    # create task object? or just append all to JSON file.

def update_task(task_id):
    # TODO update existing task

def delete_task(task_id):
    # TODO delete existing task
    # TODO optional: remove task id, either shift all IDs down, or allow new task to use the now released ID



def list_tasks():
    # TODO list all tasks
    
def list_tasks_complete():
    
def list_tasks_incomplete():

def list_tasks_in_progress():






def main():
    parser = argparse.ArgumentParser(description="A simple CLI task tracking tool.")



