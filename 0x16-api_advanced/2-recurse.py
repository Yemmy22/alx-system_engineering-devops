#!/usr/bin/python3
"""
A recures function module
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a
    list containing the titles of all hot articles
    or None.
    """
    headers = {"User-Agent": "Ubuntu_20.04_LTS"}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        params = {"after": after}
    else:
        params = {}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data")
        posts = data.get("children")

        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data.get("after", None)

        if after:
            return recurse(subreddit, hot_list, after)
        if hot_list:
            return hot_list
    except Exception:
        return None
