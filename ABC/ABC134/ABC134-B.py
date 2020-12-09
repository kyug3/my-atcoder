import sys
input = sys.stdin.readline

N, D = map(int, input().split())

for i in range(1, N + 1):
    if (D * 2 + 1) * i >= N:
        print(i)
        break