S = input()
ans = "Good"
for n in range(1, 4):
    if S[n-1] == S[n]:
        ans = "Bad"
print(ans)