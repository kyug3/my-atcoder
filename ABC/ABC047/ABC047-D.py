N, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
ma = 0
dif = 0
for i in range(N-1, -1, -1):
    if ma < A[i]:
        ma = A[i]
        continue
    if ma - A[i] == dif:
        ans += 1
    elif ma - A[i] > dif:
        ans = 1
        dif = ma - A[i]

print(ans if ans else 1)
