N = int(input())
S = list(input())
ans = 0
for n in range(2, N):
    if S[n - 2: n + 1] == ['A', 'B', 'C']:
        ans += 1

print(ans)