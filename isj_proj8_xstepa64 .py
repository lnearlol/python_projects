#!/usr/bin/env python3


def first_with_given_key(iterable, key=lambda x: x):
    spisek = []
    klice = []
    for i in iterable:
        if key(i) not in klice:  
            klice.append(key(i))
            spisek.append(i)
    return spisek
