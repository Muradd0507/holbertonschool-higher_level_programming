#!/usr/bin/python3
"""
URL fetching
"""
import requests

url = 'https://intranet.hbtn.io/status'
head = {'cfclearance': 'true'}
req = requests.get(url, headers=head)
print("Body response:\n")
print(f"\t- {type(req)}")
print(f"\t- {req.text}")
