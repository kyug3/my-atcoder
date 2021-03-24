from collections import deque

K = int(input())
queue = deque(n for n in range(1, 10))
k = 0
while True:
    x = queue.popleft()
    k += 1
    if k == K:
        print(x)
        break
    if x % 10 != 0:
        queue.append(x * 10 + x % 10 - 1)
    queue.append(x * 10 + x % 10)
    if x % 10 != 9:
        queue.append(x * 10 + x % 10 + 1)
