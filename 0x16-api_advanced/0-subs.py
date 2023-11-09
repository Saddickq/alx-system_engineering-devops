#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ function """

    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user = {'User-Agent': 'Dawuni'}
    response = requests.get(api_url, headers=user)
    if response.status_code == 200:
        data = response.json().get('data')
        return data.get('subscribers')
    return 0
