import sys
input = sys.stdin.readline

N, K = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for height in h:
    if height >= K:
        ans += 1
print(ans)