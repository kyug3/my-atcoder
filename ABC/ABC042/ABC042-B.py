N, L = map(int, input().split())
lst = [input() for _ in range(N)]
lst.sort()
print(''.join(lst))