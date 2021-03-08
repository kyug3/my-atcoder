from itertools import groupby

def RLE(s: str) -> list:
    encoded = []
    for key, group in groupby(s):
        encoded.append([key, len(list(group))])
    return encoded

N, K = map(int, input().split())
S = input()
rle = RLE(S)
group = max(1, len(rle) - (2*K))
print(N - group)