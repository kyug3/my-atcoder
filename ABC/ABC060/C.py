N, T = map(int, input().split())
t = list(map(int, input().split()))

lst = []
last = 0
for x in t:
    lst.append(min(T, x - last))
    last = x

print(sum(lst) + T)
