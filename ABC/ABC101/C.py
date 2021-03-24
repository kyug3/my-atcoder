import math
N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1 + math.ceil((N-K) / (K-1))
print(ans)