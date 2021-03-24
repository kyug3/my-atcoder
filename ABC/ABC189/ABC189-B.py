N, X = map(int, input().split())
X *= 100

al = 0
for n in range(1, N + 1):
    v, p = map(int, input().split())
    al += v * p
    if al > X:
        print(n)
        break
else:
    print(-1)