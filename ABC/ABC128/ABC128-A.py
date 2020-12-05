import sys
input = sys.stdin.readline

A, P = map(int, input().split())
print((A * 3 + P) // 2)