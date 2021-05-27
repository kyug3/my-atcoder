N = int(input())
A = list(map(int, input().split()))
BIT = [0] * (N+1)

def add(i, x):
    # 1-indexed
    # i番目の要素にxを加える
    while i <= N:
        BIT[i] += x
        i += i & -i

def out(i):
    # 1-indexed
    # i番目の要素までの総和を返す
    ans = 0
    while i > 0:
        ans += BIT[i]
        i -= i & -i
    return ans