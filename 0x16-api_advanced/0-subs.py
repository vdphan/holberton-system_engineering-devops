#!/usr/bin/python3
"""Write a function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    r = requests.get('https://www.reddit.com/r/programming/about.json')
    if r:
        return r.json().get('data').get('subscribers')
    else:
        return 0
