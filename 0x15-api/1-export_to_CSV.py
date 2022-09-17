#!/usr/bin/python3
"""
    Gather data from an APIand export ot CSV
"""

import csv
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
    for task in tasks_req:
        if task.get("userId") == usrId:
            if task.get("completed") is True:
                tasks_done.append(task.get("title"))
                tasks_done_no += 1
        tasks_total += 1

    filename = employ_id + ".csv"
    with open(filename, "w") as my_file:
        csv_writer = csv.writer(my_file, quoting=csv.QUOTE_ALL, quotechar='"')
        for task2 in tasks_req:
            row = [usrId, usrname, task2.get("completed"), task2.get("title")]
            csv_writer.writerow(row)
