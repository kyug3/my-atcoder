N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (K+1)

for i in range(K+1):
    for j in range(N):
        if i - A[j] >= 0 and dp[i-A[j]] == 0:
            dp[i] = 1

print('First' if dp[-1] else 'Second')