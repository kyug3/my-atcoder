N, M = map(int, input().split())
x = M * 1900 + (N - M) * 100
p = 2 ** M
print(x * p)