# N = 配列の長さ
# data[N] が初期配列の 0 に対応する

#N = int(input())
#data = [[-1, 2**31-1] for _ in range((2*N+1))]

def update(l, r, v):
    # 区間[l, r) を v に変更する
    # vはtuple
    L = l + N
    R = r + N
    while L < R:
        if R % 2 == 1:
            data[R-1] = v
            r -= 1
        if L % 2 == 1:
            data[L] = v
            L += 1
        L //= 2; R //= 2

def query(x):
    # x の値を求める
    # data[idx][0]が大きいものほど新しい
    idx = x + N
    ans = data[idx]
    while True:
        idx //= 2
        if idx == 0:
            break
        if ans[0] < data[idx][0]:
            ans = data[idx]
    return ans[1]


# AOJ DSL_2_D
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_D

N, Q = map(int, input().split())
data = [(-1, 2**31-1) for _ in range(2*N+1)]
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        l, r, x = q[1:]
        update(l, r+1, (i, x))
    else:
        print(query(q[1]))