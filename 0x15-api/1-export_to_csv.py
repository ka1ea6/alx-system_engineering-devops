#!/usr/bin/python3
"""
Module for interacting with a RESTful API for
returning an employees TODO list progress
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = "https://jsonplaceholder.typicode.com"
        employee_id = int(sys.argv[1])

        csv_headers = ['USER_ID', 'USERNAME',
                       'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        user = requests.get(
            "{}/users/{}".format(url, employee_id)).json()
        todos = requests.get(
            "{}/users/{}/todos/".format(url, employee_id)).json()

        username = user.get('username')
        rows = []
        for todo in todos:
            rows.append({'USER_ID': employee_id, 'USERNAME': username,
                        'TASK_COMPLETED_STATUS': todo.get('completed'),
                         'TASK_TITLE': todo.get('title')})

        with open("{}.csv".format(employee_id), 'w') as f:
            writer = csv.DictWriter(f, fieldnames=csv_headers)
            writer.writerows(rows)

    else:
        print("Usage: ./1-export_to_csv.py <employee_id>")
