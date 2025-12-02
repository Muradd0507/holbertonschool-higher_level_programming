#!/usr/bin/python3
"""
URL fetching
"""
import usrllib.request

url = 'https://intranet.hbtn.io/status'

with request.urlopen(url) as u:
    res = u.read().decode('utf-8')
    print(res)
