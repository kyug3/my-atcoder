N = int(input())
csf = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    ans = csf[i][1] + csf[i][0]
    for j in range(i + 1, N - 1):
        ans = max(ans, csf[j][1])
        if ans % csf[j][2] == 0:
            ans += csf[j][0]
        else:
            ans += (csf[j][2] - ans % csf[j][2]) + csf[j][0]
    print(ans)
print(0)