import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M = li()
if N == 2:
    print(1)
    exit()
A = li()
dic = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

dp = [0] * (N+2)
for i in A:
    dp[dic[i]] = max(dp[dic[i]], i)

for i in range(2, N+1):
    if dp[i] == 0:
        continue
    for j in A:
        if i + dic[j] > N:
            continue
        dp[i+dic[j]] = max(dp[i+dic[j]], dp[i]*10 + j)

print(dp[N])