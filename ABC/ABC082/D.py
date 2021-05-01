import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

S = input().rstrip()
x, y = li()

from itertools import groupby

def RLE(s: str) -> list:
    encoded = []
    for key, group in groupby(s):
        encoded.append([key, len(list(group))])
    return encoded

a = 8002
S = RLE(S)
tf = True
dpx = [[0] * (16005) for _ in range(2)]
if S[0][0] == 'F':
    dpx[0][S[0][1] + a] = 1
    S = S[1:]
else:
    dpx[0][0+a] = 1

dpy = [[0] * (16005) for _ in range(2)]
dpy[0][0+a] = 1
countx = 0
county = 0
for s, i in S:
    if s == 'T':
        for _ in range(i):
            tf = not tf
        continue
    if tf:
        now = countx % 2
        nex = (countx + 1) % 2
        for j in range(16005):
            if dpx[now][j] == 1:
                dpx[nex][j+i] = 1
                dpx[nex][j-i] = 1
        countx += 1
        dpx[now] = [0] * (16005)
    else:
        now = county % 2
        nex = (county+1) % 2
        for j in range(16005):
            if dpy[now][j] == 1:
                dpy[nex][i+j] = 1
                dpy[nex][j-i] = 1
        county += 1
        dpy[now] = [0] * (16005)

if dpx[(countx) % 2][x+a] and dpy[(county) % 2][y+a]:
    print('Yes')
else:
    print('No')