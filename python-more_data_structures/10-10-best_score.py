#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:     # boşdursa və ya None-dursa
        return None

    best_key = None
    best_value = float('-inf')   # ən kiçik mümkün başlanğıc

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
