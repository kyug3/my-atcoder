import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

ans = 0
for n in range(2, n):
    if p[n - 2] < p[n - 1] < p[n]:
        ans += 1
    elif p[n - 2] > p[n - 1] > p[n]:
        ans += 1
print(ans)