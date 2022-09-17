#!/usr/bin/python3
"""
    Gather data from an APIand export ot CSV
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    employ_id = argv[1]
    employ_url = "https://jsonplaceholder.typicode.com/users/{}"\
                 .format(employ_id)
    tasks_url = employ_url + "/todos"
    employ_req = requests.get(employ_url).json()
    tasks_req = requests.get(tasks_url).json()
    name = employ_req.get("name")
    usrname = employ_req.get("username")
    usrId = int(argv[1])
    tasks_total = 0
    tasks_done = []
    tasks_done_no = 0
    tasks_list = []
    for task in tasks_req:
        row_dict = {}
        if task.get("userId") == usrId:
            row_dict["task"] = task.get("title")
            row_dict["completed"] = task.get("completed")
            row_dict["username"] = usrname
            tasks_list.append(row_dict)
        user_dict = {usrId: tasks_list}
    filename = employ_id + ".json"
    with open(filename, "w") as my_file:
        json.dump(user_dict, my_file)
