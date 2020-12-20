from collections import deque

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
A_sum = sum(A)
A = deque(A)
B = deque(map(int, input().split()))
ans = 0
count_a = N
count_b = 0

while True:
    if A_sum <= K:
        while B:
            if A_sum + B[0] <= K:
                b = B.popleft()
                A_sum += b
                count_b += 1
            else:
                break
        ans = max(ans, count_a + count_b)
    if not A:
        break
    a = A.pop()
    A_sum -= a
    count_a -= 1

print(ans)