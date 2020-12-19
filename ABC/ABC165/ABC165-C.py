from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]
lst = [n for n in range(1, M + 1)]
ans = 0
for A in combinations_with_replacement(lst, N):
    count = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            count += d
    ans = max(ans, count)
print(ans)