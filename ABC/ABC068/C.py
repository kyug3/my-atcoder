N, M = map(int, input().split())
ab = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    ab[a].add(b)
    ab[b].add(a)

for i in list(ab[0]):
    if N-1 in ab[i]:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')