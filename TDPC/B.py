import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, M = li()
# 山が空になった状態を,価値0の物が上にある状態としておく
A = li() + [0]
B = li() + [0]

# dp[i][j] = Aがi個、Bがj個とった状態から得られる価値の最大
dp = [[0] * (M+2) for _ in range(N+2)]

for a in range(N+1)[::-1]:
    for b in range(M+1)[::-1]:
        if (a + b) % 2 == 0:
            if a < N and b < M:
                dp[a][b] = max(dp[a+1][b] + A[a], dp[a][b+1] + B[b])
            elif a < N:
                dp[a][b] = dp[a+1][b] + A[a]
            else:
                dp[a][b] = dp[a][b+1] + B[b]
        else:
            if a < N and b < M:
                dp[a][b] = min(dp[a+1][b], dp[a][b+1])
            elif a < N:
                dp[a][b] = dp[a+1][b]
            else:
                dp[a][b] = dp[a][b+1]

print(dp[0][0])
