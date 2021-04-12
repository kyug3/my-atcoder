import math

R, X, Y = map(int, input().split())

dist = math.sqrt(X ** 2 + Y ** 2)
if R > dist:
    ans = 2
else:
    ans = int(-(-dist // R))
print(ans)
