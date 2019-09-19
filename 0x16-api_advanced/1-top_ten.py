#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed
for a given subreddit
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    for a given subreddit"""
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh;" +
               "Intel Mac OS X 10_14_5)" +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132" +
               "Safari/537.36"}
    r = requests.get('https://www.reddit.com/r/{}/hot.json'.
                     format(subreddit), headers=headers)
    if r.status_code == 200 and r.json().get('data').get('children'):
        c = r.json().get('data').get('children')
        l = len(c)
        count = 0
        if l > 10:
            count = 10
        else:
            count = l
        for i in range(0, count):
            print(c[i].get('data').get('title'))
    else:
        print(None)
