N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for n in range(N):
    d = float('inf')
    x1, y1 = AB[n][0], AB[n][1]
    for m in range(M):
        x2, y2 = CD[m][0], CD[m][1]
        if d > dist(x1, y1, x2, y2):
            ans = m + 1
            d = dist(x1, y1, x2, y2)
    print(ans)
