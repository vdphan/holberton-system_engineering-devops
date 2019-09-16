#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    r = r.json()
    r1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    r1 = r1.json()
    u = dict()
    for user in r:
        l = []
        for task in r1:
            if task.get("userId") == user.get("id"):
                d = dict()
                d["task"] = task.get("title")
                d["completed"] = task.get("completed")
                d["username"] = user.get("username")
                l.append(d)
        user_id = user.get("id")
        u[user_id] = l
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(u, json_file)
