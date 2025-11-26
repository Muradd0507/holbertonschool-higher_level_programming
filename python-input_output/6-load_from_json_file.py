#!/usr/bin/python3
"""
OBJ TO TEXT WITH JSON
"""
import json


def load_from_json_file(filename):
    """
    OBJ TO TEXT WITH JSON
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.load(f)
