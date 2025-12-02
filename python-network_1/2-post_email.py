#!/usr/bin/python3
import urllib
import sys
"""
POSTing mail
"""

sys.argv = ['2-post_email.py', 'http://0.0.0.0:5000/post_email', 'hr@holbertonschool.com']
url = sys.argv[1]
email = sys.argv[2]
data = {'post_email': email}
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data=data)

with urllib.request.urlopen(req) as u:
    res = u.read().decode()
