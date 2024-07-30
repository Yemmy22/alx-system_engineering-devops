#!/usr/bin/python3
"""Exports employee data to csv file"""


import requests
from sys import argv


if len(argv) == 2:

    url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    todos_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    user_response = requests.get(url)
    USERNAME = user_response.json().get('username')

    todos = requests.get(todos_url)

    for todo in todos.json():
        USER_ID = todo.get('userId')
        TASK_COMPLETED_STATUS = todo.get('completed')
        TASK_TITLE = todo.get('title')
        text = '"{}","{}","{}","{}"\n'.format(
                USER_ID,
                USERNAME,
                TASK_COMPLETED_STATUS,
                TASK_TITLE
                )
        if __name__ == "__main__":
            file_name = "{}.{}".format(USER_ID, "csv")
            with open(file_name, 'a', encoding="utf8") as f:
                f.write(text)
