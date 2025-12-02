#!/usr/bin/python3
"""
POSTing email
"""
import urllib.request
import urllib.parse
import sys

sys.argv = ['2-post_email.py', 'http://0.0.0.0:5000/post_email', 'hr@holbertonschool.com']
url = sys.argv[1]
email = sys.argv[2]

# send as variable name "email"
data = {"email": email}
encoded = urllib.parse.urlencode(data).encode("utf-8")

req = urllib.request.Request(url, data=encoded)

with urllib.request.urlopen(req) as response:
    body = response.read().decode("utf-8")
    print(body)

