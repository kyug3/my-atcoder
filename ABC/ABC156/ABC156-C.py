N = int(input())
X = list(map(int, input().split()))
ans = float('inf')
for p in range(0, 101):
    dist = 0
    for x in X:
        dist += (x - p) ** 2
    ans = min(ans, dist)
print(ans)