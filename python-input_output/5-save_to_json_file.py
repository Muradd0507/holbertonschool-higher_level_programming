#!/usr/bin/python3
"""
OBJ TO TEXT WITH JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    OBJ TO TEXT WITH JSON
    """
    with open(filename, 'w', encoding='utf-8') as f:
        rep = json.dump(my_obj, f)
