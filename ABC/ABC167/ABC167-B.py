A, B, C, K = map(int, input().split())

ans = min(A, K)
K -= A + B
if K <= 0:
    print(ans)
else:
    ans -= K
    print(ans)