from collections import deque

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
queue = deque([])
ans = 0
for n, t in enumerate(T):
    if n >= K:
        x = queue.popleft()
    else:
        x = ''
    if not x == t:
        if t == 'r':
            ans += P
        elif t == 's':
            ans += R
        else:
            ans += S
    else:
        t = ''
    queue.append(t)

print(ans)
    