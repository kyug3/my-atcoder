import sys
input = sys.stdin.readline

def is_ok(r1, c1):
    if r1 + c1 == r2 + c2:
        return True
    elif r1 - c1 == r2 - c2:
        return True
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        return True
    return False

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if r1 == r2 and c1 == c2:
    print(0)
elif is_ok(r1, c1):
    print(1)
elif (r1 + c1) % 2 == (r2 + c2) % 2:
    print(2)
else:
    for i in range(-3, 4):
        for j in range(-3, 4):
            r3 = r1 + i
            c3 = c1 + j
            if is_ok(r3, c3):
                print(2)
                exit()
    print(3)