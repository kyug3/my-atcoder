am = [[0 if i == j else 10**10 for j in range(N)]
      for i in range(N)]

def floyd_warshall(num_node, am):
    # am = adjacency matrix
    for k in range(num_node):
        for i in range(num_node):
            for j in range(num_node):
                am[i][j] = min(am[i][j], am[i][k] + am[k][j])
    return am