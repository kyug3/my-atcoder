import sys
input = sys.stdin.readline

A, B = input().rstrip().split()
A = int(A)
B = int(B.replace('.', ''))
print(A * B // 100)