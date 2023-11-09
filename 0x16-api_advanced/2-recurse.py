#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.If no
results are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ function """

    api_url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    user = {'User-Agent': 'Dawuni'}
    response = requests.get(api_url, headers=user, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))

        next_page = data.get('after')
        if next_page:
            return recurse(subreddit, hot_list, after=next_page)
        else:
            return hot_list
    return None
