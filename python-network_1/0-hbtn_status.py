#!/usr/bin/python3
"""
dssdf
"""
import urllib.request
"""
This module is using for handling URLs
"""
url = 'https://intranet.hbtn.io/status'
req = urllib.equest.Request(url, headers={'cfclearance': 'true'})
with urllib.request.urlopen(req) as url:
    u = url.read().decode('utf-8')
    print(u)
