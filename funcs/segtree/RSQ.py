# N = 配列の長さ
# data[N] が初期配列の 0 に対応する

#N = int(input())
#data = [0] * (2*N+1)

def query(l, r):
    # 区間[l, r) の合計を返す
    L = l + N
    R = r + N
    ans = 0
    while L < R:
        if R % 2 == 1:
            ans += data[R-1]
            r -= 1
        if L % 2 == 1:
            ans += data[L]
            L += 1
        L //= 2; R //= 2
    return ans

def update(x, v):
    # xにvを加算する
    idx = x + N
    data[idx] += v
    while True:
        idx //= 2
        if idx == 0:
            break
        data[idx] += v


# AOJ DSL_2_B
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B

N, Q = map(int, input().split())
data = [0] * (2*N+1)

for _ in range(Q):
    q, x, y = map(int, input().split())
    if q == 0:
        update(x, y)
    else:
        print(query(x, y+1))