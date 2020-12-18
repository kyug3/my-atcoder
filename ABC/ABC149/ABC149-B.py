import sys
input = sys.stdin.readline

A, B, K = map(int, input().split())
A_rest = max(0, A - K)
B_rest = max(0, B - max(0, K - A))
print(A_rest, B_rest)