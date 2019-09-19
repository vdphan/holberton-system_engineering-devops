#!/usr/bin/python3
"""Write a function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit))
    if r.status_code == 200 and r.json().get('data').get('subscribers'):
        return r.json().get('data').get('subscribers')
    else:
        return 0
