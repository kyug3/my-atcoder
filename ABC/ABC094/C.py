N = int(input())
X = list(map(int, input().split()))
X2 = sorted(X)
a = X2[N//2 - 1]
b = X2[N//2]
for x in X:
    if x <= a:
        print(b)
    else:
        print(a)