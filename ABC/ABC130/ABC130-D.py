N, K = map(int, input().split())
A = list(map(int, input().split()))
B = []
b = 0
for a in A:
    b += a
    B.append(b)
ans = 0
last_j = 0
minus = 0
for i in range(N):
    for j in range(last_j, N):
        if B[j] - minus >= K:
            ans += N - j
            break
    minus += A[i]
    last_j = j

print(ans)