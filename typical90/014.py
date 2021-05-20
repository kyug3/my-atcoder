import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
A = li()
B = li()
A.sort()
B.sort()

ans = 0
for i in range(N):
    ans += abs(A[i] - B[i])
print(ans)