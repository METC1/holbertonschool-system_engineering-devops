#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Function to get number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'Holberton_student_sample_request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    print("Response: {}".format(response))
    if str(response) != "<Response [200]>":
        return 0
    json_response = response.json()
    subscribers = json_response.get("data").get("subscribers")
    return subscribers
