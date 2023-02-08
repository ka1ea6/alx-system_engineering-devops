#!/usr/bin/python3
'''Module for interacting with a RESTful API for
returning an employees TODO list progress'''

import sys
import requests
import csv

if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        csv_headers = ['USER_ID', 'USERNAME',
                       'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos/")

        username = user.json()['username']
        rows = []
        for todo in todos.json():
            rows.append({'USER_ID': employee_id, 'USERNAME': username,
                        'TASK_COMPLETED_STATUS': todo['completed'],
                         'TASK_TITLE': todo['title']})

        with open(f"{employee_id}.csv", 'w') as f:
            writer = csv.DictWriter(f, fieldnames=csv_headers)
            writer.writerows(rows)

    else:
        print("Usage: ./1-export_to_csv.py <employee_id>")
