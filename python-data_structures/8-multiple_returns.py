#!/usr/bin/python3
def multiple_returns(sentence):
    t = ()
    t = list(t)
    if (len(sentence) == 0):
        a2 = None
    else:
        a2 = sentence[0]
    a1 = len(sentence)
    t.append(a1)
    t.append(a2)
    t = tuple(t)
    return t
