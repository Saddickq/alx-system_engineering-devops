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
    try:
        u_id = int(argv[1])
    except Exception:
        return

    api_url = f"https://jsonplaceholder.typicode.com/users/{u_id}"

    with urllib.request.urlopen(api_url) as response:
        data_dict = json.loads(response.read().decode("utf-8"))
        emp_name = data_dict.get("username")

    todo_api = 'https://jsonplaceholder.typicode.com/{}'.format("todos")
    list_dict = []

    with urllib.request.urlopen(todo_api) as response:
        list_dict = json.loads(response.read().decode("utf-8"))

    json_list = []
    for value in list_dict:
        json_dict = {}
        if value.get('userId') == u_id:
            json_dict['task'] = value.get('title')
            json_dict['completed'] = value.get('completed')
            json_dict['username'] = emp_name
            json_list.append(json_dict)

    dictionary = {u_id: json_list}

    filename = '{}.json'.format(u_id)
    with open(filename, mode='w') as my_file:
        json.dump(dictionary, my_file)


if __name__ == '__main__':
    main()
