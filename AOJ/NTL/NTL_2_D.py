a, b = map(int, input().split())
if (a > 0 or b > 0) and not (a > 0 and b > 0):
    a, b = abs(a), abs(b)
    print(-(a // b))
else:
    a, b = abs(a), abs(b)
    print(a // b)