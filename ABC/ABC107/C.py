N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = float('inf')
for i in range(N-K+1):
    left = X[i]
    right = X[i+K-1]
    total = min(abs(left) + abs(right-left), abs(right) + abs(left-right))
    ans = min(ans, total)

print(ans)