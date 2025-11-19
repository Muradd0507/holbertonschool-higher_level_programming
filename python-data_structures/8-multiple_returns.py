#!/usr/bin/python3
def multiple_returns(sentence):
    t = ()
    t = list(t)
    a1 = len(sentence)
    a2 = sentence[0]
    t.append(a1)
    t.append(a2)
    t = tuple(t)
    return t
