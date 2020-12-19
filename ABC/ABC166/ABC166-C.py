N, M = map(int, input().split())
H = list(map(int, input().split()))
route = [[] for n in range(N)]
for m in range(M):
    A, B = map(int, input().split())
    route[A - 1].append(B - 1)
    route[B - 1].append(A - 1)
ans = 0
for i in range(N):
    Hi = H[i]
    for j in route[i]:
        if H[j] >= Hi:
            break
    else:
        ans += 1
print(ans)