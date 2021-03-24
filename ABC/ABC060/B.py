A, B, C = map(int, input().split())

for i in range(1, 10 ** 5 + 1):
    if A * i % B == C:
        print('YES')
        break
else:
    print('NO')