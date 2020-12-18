N = int(input())
P = list(map(int, input().split()))
low = P[0]
ans = 1
for n in range(1, N):
    if P[n] <= low:
        ans += 1
        low = P[n]
print(ans)