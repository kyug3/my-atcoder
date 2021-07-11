import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N = input()
K = int(input())

# dp[i][j][k]
# i桁目まで見て
# j N以下が確定してるかどうか
# k 0以外の数
dp = [[[0] * 5 for _ in range(2)]
      for _ in range(len(N)+1)]
dp[0][0][0] = 1

for i in range(len(N)):
    for j in range(2):
        for k in range(4):
            lim = int(N[i])
            if j == 1:
                dp[i+1][j][k+1] += dp[i][j][k] * 9 # 0以外を選ぶ
                dp[i+1][j][k] += dp[i][j][k] # 0を選ぶ
            elif lim == 0:
                dp[i+1][j][k] += dp[i][j][k]
            else:
                dp[i+1][j][k+1] += dp[i][j][k] # limを選ぶ
                dp[i+1][1][k+1] += dp[i][j][k] * (lim-1) # 1以上lim未満を選ぶ
                dp[i+1][1][k] += dp[i][j][k] # 0を選ぶ

print(dp[-1][0][K] + dp[-1][1][K])
#print(dp)