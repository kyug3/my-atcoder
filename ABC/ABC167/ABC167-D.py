N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
seen = [0 for n in range(N + 1)]
seen[1] = 1
routes = [1]

n = 1
count = 0
while True:
    a = A[n]
    if seen[a]:
        idx = routes.index(a)
        break
    count += 1
    routes.append(a)
    seen[a] = 1
    n = a
    if count == K:
        print(n)
        exit()

len_loop = len(routes) - idx
routes = routes[idx:]
print(routes[(K - idx) % len(routes)])