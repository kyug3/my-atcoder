import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, S = li()
dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1
AB = []
for i in range(1, N+1):
    A, B = li()
    AB.append((A, B))
    for j in range(S+1):
        if dp[i-1][j]:
            if j + A <= S:
                dp[i][j+A] = 1
            if j + B <= S:
                dp[i][j+B] = 1

if dp[N][S] == 0:
    print('Impossible')
    exit()

ans = []
now = S
for i in range(1, N+1)[::-1]:
    A, B = AB[i-1]
    if (now - A) >= 0 and dp[i-1][now-A]:
        ans.append('A')
        now -= A
    else:
        ans.append('B')
        now -= B
print(''.join(ans[::-1]))

