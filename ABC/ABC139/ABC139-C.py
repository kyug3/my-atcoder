import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
ans = 0
now = 0
for n in range(N - 1):
    if H[n] >= H[n + 1]:
        now += 1
    else:
        ans = max(ans, now)
        now = 0
print(max(ans, now))
