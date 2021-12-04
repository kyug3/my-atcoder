import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))
from collections import defaultdict

N, K = li()
A = li()

S = [0]
for a in A:
    S.append((S[-1] + a) % K)

ans = 0
dic = defaultdict(int)
for i in range(N+1):
    if i >= K:
        dic[(S[i-K]-(i-K)) % K] -= 1
    a = (S[i]-i) % K
    ans += dic[a]
    dic[(S[i]-i) % K] += 1
    
print(ans)
