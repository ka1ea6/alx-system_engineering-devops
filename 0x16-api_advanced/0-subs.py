#!/usr/bin/python3
'''Function to return the number of subscribers to a subreddit
using the Redit API'''


import requests
import json


def number_of_subscribers(subreddit):
    '''Funciton to get the number of subscirbers'''

    req_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(url=req_url, allow_redirects=False, headers=header)

    if res.status_code == 404:
        return 0
    return res.json().get('data').get('subscribers')
