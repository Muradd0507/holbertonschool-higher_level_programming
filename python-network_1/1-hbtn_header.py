#!/usr/bin/python3
import urllib
import sys
"""
Take URLs
"""
url = sys.argv[1]

with urllib.request.urlopen(url) as u:
    value = response.headers.get("X-Request-Id")
    print(value)
