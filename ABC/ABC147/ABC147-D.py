import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())

A = li()
a = 1
ans = 0
for j in range(60):
    count0 = 0
    count1 = 0
    for i in range(N):
        x = A[i]
        if (x >> j) & 1:
            ans += count0 * a
            ans %= mod
            count1 += 1
        else:
            ans += count1 * a
            ans %= mod
            count0 += 1
    a *= 2
    a %= mod

print(ans)