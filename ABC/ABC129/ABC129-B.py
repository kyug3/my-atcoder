import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))

ans = 10**9
for n in range(1, N):
    dif = abs(sum(W[:n]) - sum(W[n:]))
    ans = min(ans, dif)
print(ans)