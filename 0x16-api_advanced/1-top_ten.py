#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ function """

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    user = {"User-Agent": "Dawuni"}
    response = requests.get(api_url, headers=user)
    if response.status_code == 200:
        data_list = response.json().get('data').get('children')
        for post in data_list:
            print(post.get('data').get('title'))
