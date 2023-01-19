#!/usr/bin/python3
'''Python script that takes in a URL
sends a request to the URL and displays
the body of the response'''

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    res = requests.get(url)

    if res.ok:
        print(res.text)
    else:
        print(f"Error code: {res.status_code}")
