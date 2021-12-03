import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i * 10000 / N

print(ans)