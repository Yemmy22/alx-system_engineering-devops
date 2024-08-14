#!/usr/bin/python3
"""
A count_words function module.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the
    title of all hot articles, and counts the
    occurrences of specified keywords.
    """
    # Set up the headers with a custom User-Agent
    headers = {"User-Agent": "Ubuntu_20.04_LTS"}

    # Define the URL with pagination (after) parameter if available
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}

    # Make the API request
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    # Check if the request was successful
    if response.status_code != 200:
        return

    # Parse the response JSON
    data = response.json().get("data", {})
    posts = data.get("children", [])

    # Initialize or update word_count dictionary
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    # Iterate through the titles of the posts and count keywords
    for post in posts:
        title = post["data"]["title"].lower().split()
        for word in word_count.keys():
            word_count[word] += title.count(word)

    # Check if there is a next page (pagination)
    after = data.get("after", None)

    # If there's a next page, recursively call the function
    if after:
        return count_words(subreddit, word_list, after, word_count)

    # If there's no next page, sort and print the results
    if word_count:
        sorted_words = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0])
                )
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")
