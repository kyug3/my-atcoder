import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N = int(input())
if N == 3:
    print(61)
    exit()
dp = [[[[[0 for _ in range(4)]
      for _ in range(4)]
      for _ in range(4)]
      for _ in range(4)]
      for _ in range(N+1)]

# AGC, ACG, GAC, A_GC, AG_C
# AGCT -> 0123

for n in range(4, N+1):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if ((i == 0 and j == 1 and k == 2)
                    or (i == 0 and j == 2 and k == 1)
                    or (i == 1 and j == 0 and k == 2)):
                    continue
                for l in range(4):
                    if ((j == 0 and k == 1 and l == 2)
                        or (j == 0 and k == 2 and l == 1)
                        or (j == 1 and k == 0 and l == 2)):
                        continue
                    if ((i == 0 and k == 1 and l == 2)
                        or (i == 0 and j == 1 and l == 2)):
                        continue
                    if n == 4:
                        dp[4][i][j][k][l] = 1
                    else:
                        dp[n][i][j][k][l] += sum(dp[n-1][j][k][l]) % mod

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][i][j][k][l]
                ans %= mod
print(ans)