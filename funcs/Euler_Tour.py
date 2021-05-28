in_ = [0] * N
out_ = [0] * N
count = 0

def dfs(n, parent):
    global count
    dist[n] = dist[parent] + 1
    dist2[dist[n]].append(n)
    count += 1
    in_[n] = count
    for x in G[n]:
        if x == parent:
            continue
        dfs(x, n)
    count += 1
    out_[n] = count
dfs(0, -1)