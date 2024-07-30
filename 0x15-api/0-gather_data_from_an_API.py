#!/usr/bin/python3
"""Returns information about an employees TODO list progress"""

from sys import argv
import requests


if len(argv) == 2:

    url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    todos_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    user_response = requests.get(url)
    EMPLOYEE_NAME = user_response.json().get('name')

    todos = requests.get(todos_url)

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    for todo in todos.json():
        TOTAL_NUMBER_OF_TASKS += 1
        if todo.get('completed'):
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(todo)


if __name__ == "__main__":
    print(f"Employee EMPLOYEE_NAME is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}): ")

    for task in TASK_TITLE:
        print("\t {}".format(task.get('title')))
