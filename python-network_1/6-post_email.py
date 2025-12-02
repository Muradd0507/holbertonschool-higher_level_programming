#!/usr/bin/python3
"""
POSTing emails with requests
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    res = requests.post(url, data=email)
    print(res)
