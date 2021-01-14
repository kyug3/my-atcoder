N, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    now_a1 = a[i]
    now_a2 = a[i + 1]
    if a[i] + a[i + 1] > x:
        a[i + 1] = max(0, x - a[i])
        ans += now_a2 - a[i + 1]
        if a[i] + a[i + 1] > x:
            a[i] = x - a[i + 1]
            ans += now_a1 - a[i]
print(ans)