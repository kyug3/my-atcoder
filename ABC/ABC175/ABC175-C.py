import sys
input = sys.stdin.readline

X, K, D = map(int, input().split())
X = abs(X)

y = min(K, X // D)
K -= y
X -= y * D

if K % 2 == 0:
    print(X)
else:
    print(D - X)