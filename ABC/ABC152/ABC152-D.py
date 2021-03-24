N = int(input())

table = [[0] * 10 for _ in range(10)]

for i in range(1, N+1):
    si = str(i)
    table[int(si[0])][int(si[-1])] += 1
ans = 0
for i in range(1, N+1):
    si = str(i)
    if si[0] == '0' or si[-1] == '0':
        continue
    ans += table[int(si[-1])][int(si[0])]
print(ans)