import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import defaultdict

N = int(input())
blue = defaultdict(int)
for i in range(N):
    s = input()
    blue[s] += 1

M = int(input())
for _ in range(M):
    t = input()
    blue[t] -= 1

ans = 0
for _, v in blue.items():
    ans = max(v, ans)
print(ans)