#!/usr/bin/python3
'''
Module for interacting with a RESTful API for
returning an employees TODO list progress
'''

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos/")

        username = user.json().get('username')
        rows = {f"{employee_id}": []}
        for todo in todos.json():
            rows[f'{employee_id}'].append({'username': username,
                                           'completed': todo.get('completed'),
                                           'task': todo.get('title')})

        with open(f"{employee_id}.json", 'w') as f:
            json.dump(rows, f)
    else:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
