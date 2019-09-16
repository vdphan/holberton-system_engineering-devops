#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(sys.argv[1]))
    r = r.json()
    r1 = requests.get('https://jsonplaceholder.typicode.com/todos/?userId={}'.
                      format(sys.argv[1]))
    r1 = r1.json()
    l = []
    for t in r1:
        d = dict()
        d["task"] = t.get("title")
        d["completed"] = t.get("completed")
        d["username"] = r.get("username")
        l.append(d)
    u = {sys.argv[1]: l}
    fname = sys.argv[1] + ".json"
    with open(fname, 'w') as json_file:
        json.dump(u, json_file)
