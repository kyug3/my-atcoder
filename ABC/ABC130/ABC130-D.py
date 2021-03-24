N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
b = 0
for a in A:
    b += a
    B.append(b)

ans = 0
last_j = 0
for i in range(N):
    for j in range(last_j, N):
        if B[j + 1] - B[i] >= K:
            ans += N - j
            last_j = j
            break
    
print(ans)