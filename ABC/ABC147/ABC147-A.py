import sys
input = sys.stdin.readline

A = map(int, input().split())
print('bust' if sum(A) >= 22 else 'win')