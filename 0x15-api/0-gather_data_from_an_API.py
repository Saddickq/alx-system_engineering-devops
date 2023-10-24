#!/usr/bin/python3
"""
a Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import urllib.request
from sys import argv
import json


def main():
    """ Main function """
    try:
        u_id = int(argv[1])
    except Exception:
        return

    api_url = f"https://jsonplaceholder.typicode.com/users/{u_id}"

    with urllib.request.urlopen(api_url) as response:
        data_dict = json.loads(response.read().decode("utf-8"))
        emp_name = data_dict.get("name")

    done = 0
    total = 0
    todo_api = 'https://jsonplaceholder.typicode.com/{}'.format("todos")
    list_dict = []

    with urllib.request.urlopen(todo_api) as response:
        list_dict = json.loads(response.read().decode("utf-8"))

    for dic in list_dict:
        if dic.get("userId") == u_id:
            total = total + 1
            if dic.get("completed"):
                done = done + 1

    print(f"Employee {emp_name} is done with tasks({done}/{total}):")
    for value in list_dict:
        if value.get('userId') == u_id and value.get("completed"):
            print("\t {}".format(value.get("title")))


if __name__ == '__main__':
    main()
