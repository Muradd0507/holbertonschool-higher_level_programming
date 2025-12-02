#!/usr/bin/python3
"""
try except with url example
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    head = {'cfclearance': 'true'}
    req = urllib.request.Request(url, headers=head)
    try:
        with urllib.request.urlopen(req) as u:
            res = u.read().decode('utf-8')
            print(res)
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code, end='')
