#!/usr/bin/python3
"""A top_ten function module."""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Ubuntu_20.04_LTS'}
    params = {'limit': 10}
    response = requests.get(
            url, params=params, headers=headers, allow_redirects=False
            )
    try:
        data = response.json().get('data').get('children')

        for ele in data:
            print(ele.get('data').get('title'))
    except Exception:
        print('None')
