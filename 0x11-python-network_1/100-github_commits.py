#!/usr/bin/python3
'''Python script to get list of commits'''

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    res = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    res_json = res.json()
    for item in res_json:
        print(f"{item.get('sha')}: \
{item.get('commit').get('author').get('name')}")
