import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if 2*N <= M:
    M -= 2*N
    print(N + (M // 4))
else:
    print(M//2)