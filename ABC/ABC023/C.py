import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))
from collections import defaultdict

R, C, K = li()
N = int(input())
Rs = [0] * (R+1)
Cs = [0] * (C+1)

RC = [[] for _ in range(R+1)]
for i in range(N):
    r, c = li()
    RC[r].append(c)
    Rs[r] += 1
    Cs[c] += 1

C_cnt = defaultdict(set)
for i in range(1, C+1):
    C_cnt[Cs[i]].add(i)

ans = 0
for i in range(1, R+1):
    k = K - Rs[i]
    ans += len(C_cnt[k])
    for j in RC[i]:
        if j in C_cnt[k]:
            ans -= 1
        if j in C_cnt[k+1]:
            ans += 1

print(ans)
