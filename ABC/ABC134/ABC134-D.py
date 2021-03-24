N = int(input())
A = list(map(int, input().split()))
balls = [0 for _ in range(N)]
ans = []
for i in reversed(range(1, N + 1)):
    num_ball = 0
    for j in range(i, N + 1, i):
        num_ball += balls[j - 1]
    if num_ball % 2 != A[i - 1] % 2:
        balls[i - 1] = 1
        ans.append(str(i))

ans.sort()
print(len(ans))
print(' '.join(ans))