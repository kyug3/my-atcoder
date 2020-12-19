N, K = map(int, input().split())
if N % K == 0:
    print(0)
else:
    print(min(abs(N % K - K), N))