C = [list(map(int, input().split())) for _ in range(3)]

a1 = 0
Bs = []
for i, c in enumerate(C[0]):
    Bs.append(c - a1)

if not (C[1][0] - Bs[0] == C[1][1] - Bs[1] == C[1][2] - Bs[2]):
    print('No')
    exit()
if not (C[2][0] - Bs[0] == C[2][1] - Bs[1] == C[2][2] - Bs[2]):
    print('No')
    exit()
print('Yes')