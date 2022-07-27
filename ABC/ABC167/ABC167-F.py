import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
各S内の()を相殺すると、
    )が連続した文字列
    (が連続した文字列
    )の連続と(の連続をこの順に連結した文字列
となり、これらについて考えればよい。
括弧列はどのようにprefixをとっても)の数が(の数を超えない性質があるので、
まず(だけの文字列を並べて、その貯金を減らさないように連結していきたい気持ちになる
"""
N = int(input())
A = []
B = []
C = []
for _ in range(N):
    S = input()
    now = []
    for s in S:
        if s == '(':
            now.append(s)
        else:
            if now and now[-1] == '(':
                now.pop()
            else:
                now.append(')')
    a = 0
    b = 0
    for s in now:
        if s == '(':
            a += 1
        else:
            b += 1
    if a and b:
        C.append((a, b))
    elif a:
        A.append(a)
    elif b:
        B.append(b)

C.sort(key=lambda x: x[1] - x[0])
now = sum(A)
ans = 'Yes'
for a, b in C:
    if now < b:
        ans = 'No'
    now -= (b - a)
now -= sum(B)
if now != 0:
    ans = 'No'
print(ans)

