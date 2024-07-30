#!/usr/bin/python3
"""exports data in the JSON format."""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictn = {}
    for user in users:
        Id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(Id)
        url = url + '/todos/'
        response = requests.get(url)
        todos = response.json()
        dictn[Id] = []
        for todo in todos:
            dictn[Id].append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w', encoding="utf8") as f:
        json.dump(dictn, f)
