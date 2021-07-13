import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from heapq import *

X, Y, A, B, C = li()
red = li()
gre = li()
oth = li()

red.sort(reverse=True)
gre.sort(reverse=True)
oth.sort(reverse=True)

H = []
heapify(H)
for r in red[:X]:
    heappush(H, r)
for g in gre[:Y]:
    heappush(H, g)

for o in oth:
    mi = heappop(H)
    if mi >= o:
        heappush(H, mi)
        break
    else:
        heappush(H, o)
print(sum(H))