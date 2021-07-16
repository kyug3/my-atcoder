import sys, math
#sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from bisect import *

N = int(input())
A = li()
INF = float('inf')
LIS = [INF] * (N+1)
ma = 0
lst = [0] * N
for i, a in enumerate(A):
    x = bisect_left(LIS, a)
    if x == ma:
        ma += 1
    lst[i] = ma
    LIS[x] = a
    

LIS2 = [INF] * (N+1)
ma = 0
lst2 = [0] * N
for i, a in enumerate(A[::-1]):
    x = bisect_left(LIS2, a)
    if x == ma:
        ma += 1
    lst2[i] = ma
    LIS2[x] = a

ans = 0
for a, b in zip(lst, lst2[::-1]):
    ans = max(ans, a+b - 1)
print(ans)