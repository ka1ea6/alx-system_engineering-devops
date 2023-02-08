#!/usr/bin/python3
"""
Module for interacting with a RESTful API for
returning an employees TODO list progress
"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    users = requests.get(
        "{}/users".format(url)).json()
    todos = requests.get(
        "{}/todos/".format(url)).json()

    usernames = {}
    rows = {}
    for user in users:
        usernames[user.get('id')] = user.get('username')
        rows[user.get('id')] = []

    for todo in todos:
        rows[todo.get("userId")].append({'username':
                                         usernames.get(todo.get('userId')),
                                         'completed': todo.get('completed'),
                                         'task': todo.get('title')})

    with open("todo_all_employees.json", 'w') as f:
        json.dump(rows, f)
