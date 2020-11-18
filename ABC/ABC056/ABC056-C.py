import sys
input = sys.stdin.readline

X = int(input())

for N in range(X+1):
    if X <= N * (2 + N - 1) / 2:
        print(N)
        exit(0)
