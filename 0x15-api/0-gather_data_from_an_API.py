#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = "https://jsonplaceholder.typicode.com"
        employee_id = int(sys.argv[1])
        user = requests.get(
            "{}/users/{}".format(url, employee_id)).json()
        todos = requests.get(
            "{}/users/{}/todos/".format(url, employee_id)).json()

        done_tasks = 0
        done_tasks_str = ""
        for todo in todos:
            if todo['completed']:
                done_tasks += 1
                done_tasks_str += "\t {}\n".format(todo.get('title'))
        print(
            "Employee {} is done with tasks({}/{}):"
            .format(user.get('name'), done_tasks, len(todos)))

        print(done_tasks_str[:-2])

    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
