#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
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
    c = 0
    for i in range(len(r1)):
        if r1[i]["completed"] is True:
            c = c + 1
            l.append(r1[i]["title"])
    print('Employee {} is done with tasks({}/{}):'.
          format(r['name'], c, len(r1)))
    for task in l:
        print("\t {}".format(task))
