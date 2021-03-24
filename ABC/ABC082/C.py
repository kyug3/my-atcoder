from collections import Counter

N = map(int, input().split())
A = list(map(int, input().split()))

C = Counter(A)
ans = 0
for x, y in C.items():
    if x < y:
        ans += y - x
    elif x > y:
        ans += y
print(ans)