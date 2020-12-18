N, K, M = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)
for n in range(0, K + 1):
    if M <= (sumA + n) / N:
        print(n)
        break
else:
    print(-1)
