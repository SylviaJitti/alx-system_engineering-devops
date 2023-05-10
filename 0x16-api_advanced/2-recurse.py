#!/usr/bin/python3
"""This is a recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found for
the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    '''Returns a list titles of all hot articles for a given subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'My Agent'}
    params = {
            'after': after,
            'count': count
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get('data')
        after = results.get('after')
        count += results.get('dist')
        for result in results.get('children'):
            hot_list.append(result.get('data').get('title'))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
