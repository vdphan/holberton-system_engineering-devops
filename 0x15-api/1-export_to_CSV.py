#!/usr/bin/python3
"""script to export data in the CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(sys.argv[1]))
    r = r.json()
    r1 = requests.get('https://jsonplaceholder.typicode.com/todos/?userId={}'.
                      format(sys.argv[1]))
    r1 = r1.json()
    fname = sys.argv[1] + ".csv"
    with open(fname, "w") as csvfile:
        c = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in r1:
            c.writerow([r['id'], r['username'], task["completed"],
                        task["title"]])
