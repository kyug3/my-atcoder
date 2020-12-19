K, N = map(int, input().split())
A = [0] + list(map(int, input().split())) + [K]
max_dist = A[1] + K - A[-2]
ans = 0
for n in range(N + 1):
    dist = A[n + 1] - A[n]
    ans += dist
    max_dist = max(max_dist, dist)
print(ans - max_dist)