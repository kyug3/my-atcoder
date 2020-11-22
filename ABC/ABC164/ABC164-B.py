import sys
input = sys.stdin.readline

A, B, C, D = map(int, input().split())

while A > 0 and C > 0:
    C -= B
    A -= D
    if C <= 0:
        print('Yes')
        exit(0)
    elif A <= 0:
        print('No')
        exit(0)
