import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))


def f(num_node, start):
    stack = [(start, -1)]
    distance = [float('inf')] * num_node
    used = [0] * num_node
    prev = [-1] * num_node
    distance[start] = 0

    while stack:
        node, pre = stack.pop()
        if used[node]:
            continue
        used[node] = 1
        prev[node] = pre
        for n in range(M+1)[::-1]:
            if node + n >= N+1 or S[node+n] == '1':
                continue
            n += node
            distance[n] = distance[node] + 1
            stack.append((n, node))
            break

    return distance, prev

def get_path(t, prev):

    path = []
    while t != -1:
        path.append(t)
        t = prev[t]
    path = path[::-1]
    return path


N, M = li()
S = input()
S = S[::-1]
d, prev = f(N+1, 0)

now = 0
ans = []
for i in range(N+1):
    if prev[i] == -1:
        now += 1
    else:
        ans.append(now)
        now = 1

if prev[-1] == -1:
    print(-1)
else:
    print(*ans[::-1])
