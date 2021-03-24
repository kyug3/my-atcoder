N = int(input())
S = input()

ans = 0
for i in range(1, N-1):
    x = set(S[:i])
    y = set(S[i:])
    ans = max(ans, len(x & y))
print(ans)