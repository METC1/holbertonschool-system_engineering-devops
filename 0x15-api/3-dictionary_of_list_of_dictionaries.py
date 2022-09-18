#!/usr/bin/python3
"""
    Gather data from an APIand export ot CSV
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    all_employ_url = "https://jsonplaceholder.typicode.com/users/"
    all_tasks_url = "https://jsonplaceholder.typicode.com/todos"
    all_employ_req = requests.get(all_employ_url).json()
    all_tasks_req = requests.get(all_tasks_url).json()
    complete_dict = {}
    for employee in all_employ_req:
        usrId = employee.get("id")
        usrname = employee.get("username")
        user_dict = []
        for task in all_tasks_req:
            row_dict = {}
            if task.get("userId") == usrId:
                row_dict["task"] = task.get("title")
                row_dict["completed"] = task.get("completed")
                row_dict["username"] = usrname
                user_dict.append(row_dict)
        complete_dict[usrId] = user_dict
    filename = "todo_all_employees.json"
    with open(filename, "w") as my_file:
        json.dump(complete_dict, my_file)
