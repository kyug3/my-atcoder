import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
c1 = [0] * (N + 1)
c2 = [0] * (N + 1)

for i in range(N):
    c, p = li()
    if c == 1:
        c1[i+1] = c1[i] + p
        c2[i+1] = c2[i]
    else:
        c1[i+1] = c1[i]
        c2[i+1] = c2[i] + p

for _ in range(int(input())):
    l, r = li()
    A = c1[r] - c1[l-1]
    B = c2[r] - c2[l-1]
    print(A, B)