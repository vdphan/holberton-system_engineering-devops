#!/usr/bin/python3
"""
recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddi
"""
import requests


def recurse(subreddit, hot_list=[], a=None):
    """a recursive funtion that returns
    a list containing the titles of all hot articles"""
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh;" +
               "Intel Mac OS X 10_14_5)" +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132" +
               "Safari/537.36"}
    r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                     format(subreddit, a),
                     headers=headers, allow_redirects=False)
    if r.status_code == 200 and r.json().get('data').get('children'):
        c = r.json().get('data').get('children')
        l = len(c)
        for i in range(0, l):
            hot_list.append(c[i].get('data').get('title'))
        if r.json().get('data').get('after'):
            return recurse(subreddit, hot_list,
                           r.json().get('data').get('after'))
        else:
            return hot_list
    else:
        return None
