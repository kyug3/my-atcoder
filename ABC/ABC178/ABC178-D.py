S = int(input())
mod = 10 ** 9 + 7
dp = [0] * (S + 1)
dp[0] = 1

for i in range(3, S + 1):
    count = 0
    for j in range(i - 2):
        count += dp[j]
    dp[i] = pow(count, 1, mod)
print(dp[S])