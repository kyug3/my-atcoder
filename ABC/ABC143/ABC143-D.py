N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N - 2):
    a = L[i]
    last_k = 2
    for j in range(i + 1, N - 1):
        b = L[j]
        for k in range(last_k, N):
            if a + b <= L[k]:
                last_k = k
                ans += k - j - 1
                break
        else:
            ans += k - j
            last_k = k
print(ans)
