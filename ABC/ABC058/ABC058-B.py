o = input()
e = input()
ans = ''

for n in range(len(o)):
    ans += o[n]
    if n == len(e):
        break
    ans += e[n]
print(ans)