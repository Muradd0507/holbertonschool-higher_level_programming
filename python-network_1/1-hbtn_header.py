#!/usr/bin/python3
import urllib
import sys
"""
Take URLs
"""
sys.argv = ['1-hbtn_header.py', 'https://intranet.hbtn.io']
url = sys.argv[1]

with urllib.request.urlopen(url) as u:
    value = response.headers.get("X-Request-Id")
    print(value)
