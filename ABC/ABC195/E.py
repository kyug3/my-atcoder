N = int(input())
S = list(input())
X = list(input())

dp = [[0] * 7 for _ in range(N+1)]
dp[-1][0] = 1
for i in range(N-1, -1, -1):
    for j in range(7):
        s1 = j * 10 % 7
        s2 = (j * 10 + int(S[i])) % 7
        if X[i] == 'T':
            if dp[i+1][s1] == 1 or dp[i+1][s2] == 1:
                dp[i][j] = 1
        else:
            if dp[i+1][s1] == 1 and dp[i+1][s2] == 1:
                dp[i][j] = 1

print('Takahashi' if dp[0][0] else 'Aoki')