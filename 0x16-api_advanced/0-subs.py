#!/usr/bin/python3
"""Write a function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh;" +
               "Intel Mac OS X 10_14_5)" +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132" +
               "Safari/537.36"}
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit), headers=headers)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    return 0
