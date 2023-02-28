#!/usr/bin/python3
'''Script to queries the Reddit API and print
 the titles of the first 10 hot posts listed for a given subreddit.'''


import requests


def top_ten(subreddit):
    '''Function to print the first 10 ht posts for a given subreddit'''

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        'limit': 10
    }

    res = requests.get(url, headers=header, params=params,
                       allow_redirects=False)

    if res.status_code == 404:
        print('None')
        return
    res_data = res.json().get('data').get('children')
    [print(child.get("data").get("title")) for child in res_data]
