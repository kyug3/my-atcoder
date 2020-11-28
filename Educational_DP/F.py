import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
ls = len(S)
lt = len(T)
dp = [[0 for _ in range(lt+1)] for _ in range(ls+1)]

for i in range(1, ls+1):
    for j in range(1, lt+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

len_ans = dp[-1][-1]
ans = ''
while len_ans > 0:
    if (S[ls-1] == T[lt-1]):
        ans += S[ls-1]
        ls -= 1
        lt -= 1
        len_ans -= 1
    else:
        if dp[ls][lt] == dp[ls-1][lt]:
            ls -= 1
        else:
            lt -= 1
print(ans[::-1])


        