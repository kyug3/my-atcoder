N, M = map(int, input().split())
if 2 * N >= M:
    print(M // 2)
else:
    ans = N
    M -= 2 * N
    ans += M // 4
    print(ans)