x, y = map(int, input().split())
xm = -x
ym = -y

a1 = a2 = a3 = a4 = float('inf')
if x < y:
    a1 = y - x
if xm <= y:
    a2 = 1 + y - xm
if x <= ym:
    a3 = 1 + ym - x
if xm <= ym:
    a4 = 2 + ym - xm

ans = min((a1, a2, a3, a4))
print(ans)