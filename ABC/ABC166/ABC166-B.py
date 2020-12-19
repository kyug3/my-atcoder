N, K = map(int, input().split())
lst = [1 for _ in range(N)]

for _ in range(K):
    d = int(input())
    for i in map(int, input().split()):
        i -= 1
        if lst[i]:
            lst[i] = 0
print(sum(lst))