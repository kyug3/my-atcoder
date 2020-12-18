N = int(input())
dic = {}
for _ in range(N):
    S = input()
    if S in dic:
        dic[S] += 1
    else:
        dic[S] = 1
m = max(dic.values())
lst = [k for k, v in dic.items() if v == m]
lst.sort()
for l in lst:
    print(l)