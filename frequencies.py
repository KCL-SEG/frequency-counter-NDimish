"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        x = str(x)
        if x in frequencies.keys():
            temp = frequencies[x]
            frequencies[x] = temp+1;
        else:
            frequencies[x] = 1
    return frequencies

