#!/usr/bin/python3
"""This is a recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found for
the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """return list of all hot posts titles of a subreddit """

    headers = {'User-agent': 'my agent'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
            subreddit, after)
    posts = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        posts = posts.json()['data']
        after = posts['after']
        posts = posts['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)
