A, B, C = map(int, input().split())

if A == 7:
    if B == C == 5:
        print('YES')
        exit()
elif B == 7:
    if A == C == 5:
        print('YES')
        exit()
elif C == 7:
    if A == B == 5:
        print('YES')
        exit()
print('NO')