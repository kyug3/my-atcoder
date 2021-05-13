import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, Q = li()
XY = [li() for _ in range(N)]
A = [i + j for i, j in XY]
B = [i - j for i, j in XY]
maxA = max(A)
minA = min(A)
maxB = max(B)
minB = min(B)

for i in range(Q):
    q = int(input())
    q -= 1
    x = [maxA - A[q],
         A[q] - minA,
         maxB - B[q],
         B[q] - minB]
    print(max(x))
