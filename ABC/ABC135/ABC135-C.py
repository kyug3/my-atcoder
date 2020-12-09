import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
last = 0
for n in range(N):
    ans += min(last, A[n])
    a_rest = max(A[n] - last, 0)
    if a_rest < B[n]:
        ans += a_rest
        last = B[n] - a_rest
    else:
        ans += B[n]
        last = 0
ans += min(A[-1], last)
print(ans)