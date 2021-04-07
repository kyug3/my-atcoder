def area(A):
    a = 0
    for i in range(-1, len(A) - 1):
        a += (A[i][0] - A[i+1][0]) * (A[i][1] + A[i+1][1])
    return abs(a) / 2

vs = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    vs.append((x, y))

print(area(vs))