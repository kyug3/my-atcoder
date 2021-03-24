N = int(input())
A = list(map(int, input().split()))

ma = max(A)
A.remove(ma)
mi = float('-inf')
for a in A:
    x = min(ma - a, ma - abs(ma - a))
    if mi < x:
        mi = x
        ans = a
print(ma, ans)