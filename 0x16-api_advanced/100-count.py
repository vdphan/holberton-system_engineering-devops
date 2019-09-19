#!/usr/bin/python3
"""
a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, a=None, d={}):
    """
    recursive function prints a sorted count of given keywords
    """
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh;" +
               "Intel Mac OS X 10_14_5)" +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132" +
               "Safari/537.36"}
    r = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                     format(subreddit, a),
                     headers=headers, allow_redirects=False)
    low_list = []
    for x in word_list:
        if x == "Java":
            low_list.append(x)
        else:
            low_list.append(x.lower())
    if r.status_code == 200 and r.json().get('data').get('children'):
        c = r.json().get('data').get('children')
        l = len(c)
        for i in range(0, l):
            t_list = c[i].get('data').get('title').lower().split()
            for word in low_list:
                if word not in t_list:
                    print
                else:
                    for t in t_list:
                        if t == word:
                            if word not in d:
                                d[word] = 1
                            else:
                                d[word] += 1
        if r.json().get('data').get('after'):
            return count_words(subreddit, word_list,
                               r.json().get('data').get('after'), d)
        else:
            for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0])):
                print("{}: {}".format(k, v))
    else:
        print
