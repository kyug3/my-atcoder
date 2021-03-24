N, A, B = map(int, input().split())
X = list(map(int, input().split()))
ans = 0
for n in range(N - 1):
    ans += min((X[n + 1] - X[n]) * A, B)
print(ans)