#!/usr/bin/python3
"""
URL fetching
"""
import usrllib.request

url = 'https://intranet.hbtn.io/status'
head = {'cfclearance': 'true'}
req = request.Request(url, headers=head)
with request.urlopen(req) as u:
    res = u.read().decode('utf-8')
    print(res)
