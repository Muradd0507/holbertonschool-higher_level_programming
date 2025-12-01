#!/usr/bin/python3
"""
dssdf
"""
import urllib.request
"""
This module is using for handling URLs
"""

with urllib.request.urlopen('https://intranet.hbtn.io/status') as url:
    u = url.read().decode('utf-8')
    print(u)
