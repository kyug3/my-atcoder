import math
N = int(input())
A = list(map(int, input().split()))

lgcd = [0] * N # 左からi個目の要素までのgcd
last = A[0]
lgcd[0] = A[0]
for n in range(1, N):
    x = math.gcd(A[n], last)
    lgcd[n] = x
    last = x

rgcd = [0] * N
last = A[-1]
rgcd[N-1] = A[-1]
for n in range(N-2, -1, -1):
    x = math.gcd(A[n], last)
    rgcd[n] = x
    last = x

ans = max(lgcd[-2], rgcd[1])
for n in range(1, N-1):
    ans = max(ans, math.gcd(lgcd[n-1], rgcd[n+1]))
print(ans)
