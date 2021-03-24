N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (N + 1)
for a in A:
    B[a] += 1

k = min(K, B[0])
ans = 0
for i, b in enumerate(B[1:]):
    i += 1
    if b == 0:
        ans += k * i
        break
    if b < k:
        ans += (k - b) * i
        k = b
print(ans)
