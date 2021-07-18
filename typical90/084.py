import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
S = input()
total = (1 + N-1) * (N-1) // 2

from itertools import groupby

def RLE(s: str) -> list:
    encoded = []
    for key, group in groupby(s):
        encoded.append([key, len(list(group))])
    return encoded

S = RLE(S)
for _, i in S:
    total -= (1 + i-1) * (i-1) // 2
print(total)