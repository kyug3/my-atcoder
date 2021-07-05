import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

A, B = input().rstrip().split()
A = str(int(A) - 1)
def f(x):
    dp = [[[0] * 2 for _ in range(2)]
           for _ in range(len(x)+1)]
    dp[0][0][0] = 1
    for i in range(len(x)):
        n = int(x[i])
        for j in range(2):
            for k in range(2):
                for d in range(10 if j else n+1):
                    dp[i+1][j or (d < n)][k or (d==4) or (d==9)] += dp[i][j][k]
    return dp[-1][0][1] + dp[-1][1][1]
print(f(B) - f(A))