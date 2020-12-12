import sys
input = sys.stdin.readline

A, B = map(int, input().split())
print(max(0, A - B * 2))