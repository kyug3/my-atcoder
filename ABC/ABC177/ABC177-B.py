import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
ans = 10**10
for i in range(len(T), len(S)+1):
    count = 0
    for n, s in enumerate(S[i-len(T): i]):
        if T[n] != s:
            count += 1
    ans = min(ans, count)
print(ans)