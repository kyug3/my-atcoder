import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
maxA = max(A)
if A.count(maxA) > 1:
    for _ in range(N):
        print(maxA)
else:
    idx = A.index(maxA)
    for i in range(N):
        if i == idx:
            print(sorted(A)[-2])
        else:
            print(maxA)
