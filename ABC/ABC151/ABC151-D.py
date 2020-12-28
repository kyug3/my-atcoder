from collections import deque

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))

def bfs(start):
    queue = deque([start])
    count = 0
    H_plus = [1, -1, 0, 0]
    W_plus = [0, 0, 1, -1]
    seen = [[-1] * W for _ in range(H)]
    seen[start[0]][start[1]] = 0
    while queue:
        count += 1
        h, w = queue.popleft()
        for i in range(4):
            next_h, next_w = h + H_plus[i], w + W_plus[i]
            if next_h < 0 or next_w < 0 or next_h >= H or next_w >= W:
                continue
            elif S[next_h][next_w] == '#' or seen[next_h][next_w] > -1:
                continue
            seen[next_h][next_w] = seen[h][w] + 1
            queue.append([next_h, next_w])
    max_move = max([max(x) for x in seen])
    return max_move

ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        c = bfs([h, w])
        ans = max(ans, c)

print(ans)