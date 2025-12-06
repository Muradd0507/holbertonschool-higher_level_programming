#!/usr/bin/python3
import requests
import sys

header = {'cfclearance': 'true'}
q = sys.argv[1] if len(sys.argv) > 1 else ""
try:
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q}, headers=header)
    j = r.json()
    if not j:
        print("No result")
    else:
        print(f"[{j.get('id')}] {j.get('name')}")
except requests.exceptions.JSONDecodeError:
    print("Not a valid JSON")
