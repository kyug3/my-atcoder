N = int(input())
A = list(map(int, input().split()))
dic = {}
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

A = [0] + A
for n in range(N):
    if n + 1 in dic:
        print(dic[n + 1])
    else:
        print(0)