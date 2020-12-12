import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for n in range(N):
    i = A[n] - 1
    ans += B[i]
    if n == N - 1:
        break
    if A[n] + 1 == A[n + 1]:
        ans += C[i]
print(ans)