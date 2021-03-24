N, K = map(int, input().split())
p = list(map(int, input().split()))

s = 0
sums = [0]
ans = 0
for n in range(N):
    ev = (p[n] + 1) / 2
    s += ev
    sums.append(s)
    if n >= K - 1:
        ans = max(ans, s - sums[-(K + 1)])

print(ans)