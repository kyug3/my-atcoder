N, K = map(int, input().split())
S = input()

l_0 = []
l_1 = []
last = S[0]
count = 0
for s in S:
    if s == last:
        count += 1
    else:
        if last == '0':
            l_0.append(count)
        else:
            l_1.append(count)
        last = s
        count = 1
if last == '0':
    l_0.append(count)
else:
    l_1.append(count)

ans = 0
if S[0] == '0':
    ans = sum(l_0[:K]) + sum(l_1[:K])
    l_0 = l_0[1:]
if S[-1] == '0':
    ans = max(ans, sum(l_0[len(l_0)-K:]) + sum(l_1[len(l_1)-K:]))

s_0 = sum(l_0[:K])
s_1 = sum(l_1[:K+1])
ans = max(ans, s_0 + s_1)

for i in range(len(l_1) - K - 1):
    s_0 += l_0[i+K] - l_0[i]
    s_1 += l_1[i+K+1] - l_1[i]
    ans = max(ans, s_0 + s_1)

print(ans)