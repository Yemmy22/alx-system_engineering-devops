#!/usr/bin/python3
'''
A number_of_subscribers function module
'''

import json
import requests


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers)
    for a given subreddit.
    '''
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "ubuntu_20.04_LTS"}
    response = requests.get(base_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('subscribers')
        return data
    return 0
