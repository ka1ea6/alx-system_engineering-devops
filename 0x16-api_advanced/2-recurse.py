#!/usr/bin/python3
'''Script for containing a function for recursively querying the
Reddit API'''


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    '''Function to recursively query the reddit api and
    return the hottest posts within a subreddit'''

    url = "https://www.reddit.com/r1/{}/hot/.json".format(subreddit)

    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "limit": 100,
        "after": after,
        "count": count
    }

    res = requests.get(url, headers=header, params=params,
                       allow_redirects=False)

    if res.status_code == 404:
        return None

    data = res.json().get("data")
    after = data.get("after")
    count += int(data.get("dist"))
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
