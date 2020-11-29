import sys
input = sys.stdin.readline

lst = [str(input().rstrip()) for _ in range(5)]
last = 100
last_idx = -1
for i in range(5):
    if last > int(lst[i][-1]) and int(lst[i][-1]) != 0:
        last = int(lst[i][-1])
        last_idx = i
if last_idx == -1:
    last_idx = 0
rest = int(lst[last_idx])
del lst[last_idx]

for i in range(4):
    x = int(lst[i])
    if x % 10 != 0:
        lst[i] = x + (10 - x % 10)
    else:
        lst[i] = x
print(sum(lst) + rest)