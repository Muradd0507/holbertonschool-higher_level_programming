#!/usr/bin/python3
"""Sends a POST request with an email"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    encoded = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(url, data=encoded, headers={'cfclearance': 'true'})

    with urllib.request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)
