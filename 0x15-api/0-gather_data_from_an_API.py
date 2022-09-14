#!/usr/bin/python3
"""
    Gather data from an API
"""

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
    usrId = int(argv[1])
    tasks_total = 0
    tasks_done = []
    tasks_done_no = 0
    for task in tasks_req:
        if task.get("userId") == usrId:
            if task.get("completed") is True:
                tasks_done.append(task.get("title"))
                tasks_done_no += 1
        tasks_total += 1
    print("Employee {} is done with tasks({}/{}):".format(name, tasks_done_no,
          tasks_total))
    for task in tasks_done:
        print("\t{} ".format(task))
