N, L = map(int, input().split())

def taste(L, i):
    return L + i - 1

x = 0
for n in range(N):
    x += taste(L, n+1)

dif = float('inf')
for n in range(N):
    y = x - taste(L, n+1)
    if dif > abs(x - y):
        dif = abs(x - y)
        ans = y
print(ans)