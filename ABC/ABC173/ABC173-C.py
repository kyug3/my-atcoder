from itertools import combinations

H, W, K = map(int, input().split())
grid = [list(input()) for _ in range(H)]

Hs = [i for i in range(H)]
Ws = [i for i in range(W)]
select_row = []
for i in range(H + 1):
    for x in combinations(Hs, i):
        select_row.append(set(x))
select_column = []
for i in range(W + 1):
    for x in combinations(Ws, i):
        select_column.append(set(x))
        
ans = 0
for rows in select_row:
    for columns in select_column:
        count = 0
        for i in range(H):
            if i in rows:
                continue
            for j in range(W):
                if j in columns:
                    continue
                if grid[i][j] == '#':
                    count += 1
        if count == K:
            ans += 1
print(ans)