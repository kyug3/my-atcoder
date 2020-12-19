N, M = map(int, input().split())
A = sum(map(int, input().split()))
print(max(-1, N - A))