import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)
ans = 0
for n in range(N):
    sum_A -= A[n]
    ans += (A[n] * sum_A)
print(ans % (10 ** 9 + 7))