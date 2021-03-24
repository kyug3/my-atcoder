N = int(input())
A = list(map(int, input().split()))
Ar = A[::-1]

a, b = [0] * N, [0] * N
a[0] = A[0]; b[0] = Ar[0]
for i in range(1, N):
    a[i] = a[i - 1] + A[i]
    b[i] = b[i - 1] + Ar[i]

mi = float('inf')
for i in range(N - 1):
    mi = min(mi, abs(a[i] - b[N - i - 2]))

print(mi)
