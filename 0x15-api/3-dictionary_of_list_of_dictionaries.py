#!/usr/bin/python3
'''Module for interacting with a RESTful API for
returning an employees TODO list progress'''

import requests
import json
users = requests.get(
    f"https://jsonplaceholder.typicode.com/users")
todos = requests.get(
    f"https://jsonplaceholder.typicode.com/todos")
usernames = {}
rows = {}
for user in users.json():
    usernames[user['id']] = user['username']
    rows[user['id']] = []

for todo in todos.json():
    rows[todo["userId"]].append({'username': usernames[todo['userId']],
                                 'completed': todo['completed'],
                                 'task': todo['title']})

with open(f"todo_all_employees.json", 'w') as f:
    json.dump(rows, f)
