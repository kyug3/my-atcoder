N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
for _ in range(min(N, K)):
    H.pop()
H.append(0)
print(sum(H))