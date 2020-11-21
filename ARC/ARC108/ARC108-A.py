import sys
input = sys.stdin.readline

S, P = map(int, input().split())

for m in range(1, S):
    if m ** 2 > P:
        print('No')
        break
    if float(S - m) == P / m:
        print('Yes')
        break
else:
    print('No')