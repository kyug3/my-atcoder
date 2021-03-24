H, W = map(int, input().split())
grid = []
wrow = ['.'] * W
cnt = 0
for _ in range(H):
    x = list(input())
    if x == wrow:
        cnt += 1
        continue
    grid.append(x)

wcol = ['.'] * (H - cnt)
s = set()
for w in range(W):
    if [x[w] for x in grid] == wcol:
        s.add(w)

grid = [[y for i, y in enumerate(x) if not i in s]for x in grid]
for g in grid:
    print(''.join(g))