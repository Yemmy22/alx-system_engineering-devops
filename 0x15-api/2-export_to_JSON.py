#!/usr/bin/python3
"""Exports employee data to json file"""


import json
import requests
import sys


if __name__ == '__main__':
    Id = sys.argv[1]
    b_Url = "https://jsonplaceholder.typicode.com/users"
    url = b_Url + "/" + Id

    response = requests.get(url)
    username = response.json().get('username')

    t_Url = url + "/todos"
    response = requests.get(t_Url)
    tasks = response.json()

    dictionary = {Id: []}

    for task in tasks:
        dictionary[Id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(Id), 'w') as filename:
        json.dump(dictionary, filename)
