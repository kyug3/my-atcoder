N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]


ans = 0
for i in range(2 ** K):
    bucket = [0] * 110
    for j in range(K):
        if (i >> j) & 1:
            bucket[CD[j][0]] = 1
        else:
            bucket[CD[j][1]] = 1
    cnt = 0
    for a, b in AB:
        if bucket[a] and bucket[b]:
            cnt += 1
    ans = max(ans, cnt)
print(ans)