#!/usr/bin/python3
import urllib
"""
This module is using for handling URLs
"""

with urllib.request.urlopen('https://intranet.hbtn.io/status') as url:
    u = url.read().urllib.request.decode('utf-8')
    print(u)
