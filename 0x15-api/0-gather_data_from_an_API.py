#!/usr/bin/python3
'''Module for interacting with a RESTful API for
returning an employees TODO list progress'''

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos/")

        done_tasks = 0
        done_tasks_str = ""
        for todo in todos.json():
            if todo['completed']:
                done_tasks += 1
                done_tasks_str += f"\t {todo.get('title')}\n"
        print(
            f"Employee {user.json().get('name')} is done with tasks\
    ({done_tasks}/{ len(todos.json())}):")
        print(done_tasks_str[:-2])

    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
