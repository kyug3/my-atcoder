from itertools import groupby

def RLE(s: str) -> list:
    encoded = []
    for key, group in groupby(s):
        encoded.append((key, len(list(group))))
    return encoded

def RLD(l: list) -> str:
    decoded = ""
    for char, num in l:
        decoded += char * num
    return decoded

rle = RLE('RRLLLRL') 
# [['R', 2], ['L', 3], ['R', 1], ['L', 1]]

rld = RLD(rle)
# RRLLLRL

print(rle, rld)