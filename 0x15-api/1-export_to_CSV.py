#!/usr/bin/python3
"""
a Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
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
        emp_name = data_dict.get("name")

    todo_api = 'https://jsonplaceholder.typicode.com/{}'.format("todos")
    list_dict = []

    with urllib.request.urlopen(todo_api) as response:
        list_dict = json.loads(response.read().decode("utf-8"))

    csv_info = []
    for value in list_dict:
        temp_dict = {}
        if value.get('userId') == u_id:
            temp_dict['userId'] = u_id
            temp_dict['name'] = emp_name
            temp_dict['completed'] = value.get('completed')
            temp_dict['title'] = value.get('title')
            csv_info.append(temp_dict)

    headers = ['userId', 'name', 'completed', 'title']
    filename = '{}.csv'.format(u_id)
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, quoting=csv.QUOTE_ALL,
                                fieldnames=headers)
        writer.writerows(csv_info)


if __name__ == '__main__':
    main()
