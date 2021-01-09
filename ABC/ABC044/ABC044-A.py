N = int(input())
K = int(input())
X = int(input())
Y = int(input())

print(X * min(K, N) + Y * max(0, N - K))