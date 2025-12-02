#!/usr/bin/python3
"""
URL fetching
"""
import requests

url = 'https://intranet.hbtn.io/status'
req = requests.get(url)
print("Body response:")
print(f"\t- type: {type(req.text)}")
print(f"\t- content: {req.text}")
