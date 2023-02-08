#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
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

        done_tasks = 0
        done_tasks_str = ""
        for todo in todos:
            if todo['completed']:
                done_tasks += 1
                done_tasks_str += f"\t {todo.get('title')}\n"
        print(
            f"Employee {user.get('name')} is done with tasks\
    ({done_tasks}/{ len(todos)}):")
        print(done_tasks_str[:-2])

    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
