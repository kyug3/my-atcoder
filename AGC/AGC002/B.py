N, M = map(int, input().split())

bucket = [1] * N
red = {0}
for _ in range(M):
    x, y = map(int, input().split())
    bucket[x-1] -= 1
    bucket[y-1] += 1
    if x-1 in red:
        red.add(y-1)
        if not bucket[x-1]:
            red.remove(x-1)
print(len(red))