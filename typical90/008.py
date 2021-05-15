import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
S = list(input().rstrip())
dp = [[0] * 8 for _ in range(N+1)]
dic = {
    'a': 0,
    't': 1,
    'c': 2,
    'o': 3,
    'd': 4,
    'e': 5,
    'r': 6,
}
last = 0
for i in range(1, N+1):
    if not S[i-1] in dic:
        continue
    idx = dic[S[i-1]] + 1
    for j in range(8):
        dp[i][j] = dp[last][j]
    if idx == 1:
        dp[i][idx] += 1
    else:
        dp[i][idx] += dp[last][idx-1]
    dp[i][idx] %= mod
    last = i

print(dp[last][-1])