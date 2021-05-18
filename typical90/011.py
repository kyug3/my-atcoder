import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
works = [li() for _ in range(N)]
works.sort()
limit = works[-1][0] + 1

dp = [[0] * (N+1) for _ in range(limit)]

for i in range(1, N+1): # i-1番目の仕事
    d, c, s = works[i-1]
    for j in range(1, limit+1): # j日目
        if d < j: # 締め切り超過
            break
        if j - c < 0: #初日に始めても終わらない
            dp[j][i] = dp[j][i-1]
            continue
        dp[j][i] = max(max(dp[j-c][i-1] + s, dp[j][i-1]), dp[j-1][i])

print(dp[-1][-1])