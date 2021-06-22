import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import deque

# 0<1 <2 > 1>0

S = list(input().rstrip())
from itertools import groupby

def RLE(s: str) -> list:
    encoded = []
    for key, group in groupby(s):
        encoded.append([key, len(list(group))])
    return encoded

S = RLE(S)
ans = 0
ln = 0
for i in range(len(S)):
    k, n = S[i]
    ans += (n) * (n-1) // 2
    if k == '>':
        ans += max(n, ln)
    ln = n
else:
    if k == '<':
        ans += n

print(ans)