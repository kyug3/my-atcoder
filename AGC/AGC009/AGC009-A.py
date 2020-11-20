import sys
input = sys.stdin.readline

N = int(input())

A = [0] * N
B = [0] * N
for n in range(N):
    a, b = map(int, input().split())
    A[n], B[n] = a, b

ans = 0
for n in reversed(range(N)):
    if A[n] == 0:
        continue
    if B[n] == 1:
        continue
    now = A[n] + ans
    if now % B[n] == 0:
        continue
    push = B[n] - (now % B[n])
    ans += push
print(ans)