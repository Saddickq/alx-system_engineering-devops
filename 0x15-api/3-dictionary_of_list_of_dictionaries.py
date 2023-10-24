#!/usr/bin/python3
"""
a Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
from sys import argv
import urllib.request


def main():
    """ Main function """

    todo_api = 'https://jsonplaceholder.typicode.com/{}'.format("todos")
    with urllib.request.urlopen(todo_api) as response:
        list_dict = json.loads(response.read().decode("utf-8"))

    users_api = f"https://jsonplaceholder.typicode.com/users"
    with urllib.request.urlopen(users_api) as response:
        users_data = json.loads(response.read().decode("utf-8"))

    dictionary = {}
    for user in users_data:
        json_list = []
        for job in list_dict:
            json_dict = {}
            if job.get('userId') == user.get('id'):
                json_dict['username'] = user.get('username')
                json_dict['task'] = job.get('title')
                json_dict['completed'] = job.get('completed')
                json_list.append(json_dict)
        dictionary[user.get('id')] = json_list

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as my_file:
        json.dump(dictionary, my_file)


if __name__ == '__main__':
    main()
