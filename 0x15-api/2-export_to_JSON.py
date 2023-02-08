#!/usr/bin/python3
"""
Module for interacting with a RESTful API for
returning an employees TODO list progress
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = "https://jsonplaceholder.typicode.com"

        employee_id = int(sys.argv[1])
        user = requests.get(
            f"{url}/users/{employee_id}").json()
        todos = requests.get(
            f"{url}/users/{employee_id}/todos/").json()

        username = user.get('username')
        rows = {f"{employee_id}": []}
        for todo in todos:
            rows[f'{employee_id}'].append({'username': username,
                                           'completed': todo.get('completed'),
                                           'task': todo.get('title')})

        with open(f"{employee_id}.json", 'w') as f:
            json.dump(rows, f)
    else:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
