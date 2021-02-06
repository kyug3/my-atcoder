S = input()
N = len(S)

ans = 0
for i in range(N):
    if S[i] == 'U':
        ans += (N-1-i) + (i*2)
    else:
        ans += i + ((N-1-i) * 2)
print(ans)