N, K = map(int, input().split())
ans = 0
for n in range(1, N + 1):
    if n >= K:
        ans += 1 / N
        continue
    count = 0
    while n < K:
        n *= 2
        count += 1
    ans += (1 / N) * ((1 / 2) ** count)
print(ans)