import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def l_inp(): return list(map(int, input().split()))
def n_inp(): return map(int, input().split())

H, W = n_inp()
if H % 3 == 0 or W % 3 == 0:
    print(0)
    exit()
dif_1 = ((H // 3 + 1) * W) - (H // 3 * W)
dif_2 = ((W // 3 + 1) * H) - (W // 3 * H)

dif_3 = float('inf')
for w in range(1, W+1):
    x = H * w
    y = (H // 2) * (W - w)
    if H % 2:
        z = (H // 2 + 1) * (W - w)
    else:
        z = y
    a = max(abs(x-y), abs(x-z))
    dif_3 = min(dif_3, a)

dif_4 = float('inf')
for h in range(1, H+1):
    x = W * h
    y = (W // 2) * (H - h)
    if W % 2:
        z = (W // 2 + 1) * (H - h)
    else:
        z = y
    a = max(abs(x - y), abs(x - z))
    dif_4 = min(dif_4, a)

print(min((dif_1, dif_2, dif_3, dif_4)))