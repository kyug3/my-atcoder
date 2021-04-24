N, W = map(int, input().split())
WV = [[] for _ in range(4)]

w1, v1 = map(int, input().split())
WV[0].append(v1)
for _ in range(N-1):
    w, v = map(int, input().split())
    w -= w1
    WV[w].append(v)

for i in range(4):
    WV[i].sort(reverse=True)

ans = 0
for i in range(len(WV[0]) + 1):
    for j in range(len(WV[1]) + 1):
        for k in range(len(WV[2]) + 1):
            for l in range(len(WV[3]) + 1):
                if w1 * i + (w1+1) * j + (w1+2) * k + (w1+3) * l > W:
                    break
                x = sum(WV[0][:i]) + sum(WV[1][:j]) + sum(WV[2][:k]) + sum(WV[3][:l])
                ans = max(ans, x)
print(ans)