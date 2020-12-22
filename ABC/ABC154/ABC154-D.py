N, K = map(int, input().split())
p = list(map(int, input().split()))

lst = [0 for _ in range(N)]
for n in range(N):
    ev = (p[n] + 1) / 2
    lst[n] += ev
    if n + K < N:
        lst[n + K] -= ev

ans = 0
SUM = 0
for x in lst:
    SUM += x
    ans = max(ans, SUM)
print(ans)