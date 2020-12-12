import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
s = 0
for n in range(N):
   s += 1 / A[n]
print(1 / s)