import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
lst = ["" for _ in range(N)]

for n in range(N):
    lst[A[n] - 1] = str(n + 1)

print(" ".join(lst))