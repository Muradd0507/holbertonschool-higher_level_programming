#!/usr/bin/python3
"""
POSTing email
"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

# send as variable name "email"
data = {"email": email}
encoded = urllib.parse.urlencode(data).encode("utf-8")

req = urllib.request.Request(url, data=encoded)

with urllib.request.urlopen(req) as response:
    body = response.read().decode("utf-8")
    print(body)

