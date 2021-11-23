import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = int(input())
imos = [0] * (1000003)
for _ in range(N):
    a, b = li()
    imos[a] += 1
    imos[b+1] -= 1

for i in range(1000002):
    imos[i+1] += imos[i]

print(max(imos))