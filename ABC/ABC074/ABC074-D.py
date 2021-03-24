N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def floyd_warshall(num_node, am):
    # am = adjacency matrix
    cnt = 0
    for i in range(num_node):
        for j in range(num_node):
            flag = True
            for k in range(num_node):
                if k != i and k != j:
                    if am[i][j] == am[i][k] + am[k][j]:                   
                        flag = False
                if am[i][j] > am[i][k] + am[k][j]:
                    return -1
                am[i][j] = min(am[i][j], am[i][k] + am[k][j])
            if flag:
                cnt += am[i][j]
    return cnt // 2

cnt = floyd_warshall(N, A)
print(cnt)
