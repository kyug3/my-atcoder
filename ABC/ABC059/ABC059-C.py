N = int(input())
A = list(map(int, input().split()))

ans_1 = 0
total = 0
for i in range(N):
    total += A[i]
    if i % 2 == 0:
        if total > 0:
            continue
        x = abs(1 - total)
        ans_1 += x
        total = 1
    else:
        if total < 0:
            continue
        x = abs(-1 - total)
        ans_1 += x
        total = -1

ans_2 = 0
total = 0
for i in range(N):
    total += A[i]
    if i % 2 == 1:
        if total > 0:
            continue
        x = abs(1 - total)
        ans_2 += x
        total = 1
    else:
        if total < 0:
            continue
        x = abs(-1 - total)
        ans_2 += x
        total = -1

print(min(ans_1, ans_2))