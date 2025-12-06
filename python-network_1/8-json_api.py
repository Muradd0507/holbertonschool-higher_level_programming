#!/usr/bin/python3
"""
json api
"""
import requests
import sys


url = 'http://0.0.0.0:5000/search_user'
try:
    q = sys.argv[1]
except:
    q = ""
res = requests.post(url, data=q, method='POST')

try:
    json_data = res.json()
    if json_data == {} or json_data == []:
        print("No result")
    else:
        print("{} {}".format(json_data['id'], json_data['name']))

except requests.exceptions.JSONDecodeError:
    print("Data is not json")


