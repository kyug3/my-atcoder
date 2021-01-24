N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

dif = []
for i in range(1, M):
    dif.append(abs(X[i] - X[i-1]))
dif.sort(reverse=True)
ans = sum(dif[N-1:])
print(ans)