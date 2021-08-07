# N = 配列の長さ
# data[N] が初期配列の 0 に対応する

#N = int(input())
#data = [0] * (2*N+1)

def query(l, r):
    # 区間[l, r) の最小値を返す
    L = l + N
    R = r + N
    ans = 2**31-1
    while L < R:
        if R % 2 == 1:
            if ans > data[R-1]:
                ans = data[R-1]
            r -= 1
        if L % 2 == 1:
            if ans > data[L]:
                ans = data[L]
            L += 1
        L //= 2; R //= 2
    return ans

def update(x, v):
    # xをvに変更する
    idx = x + N
    data[idx] = v
    while True:
        idx //= 2
        if idx == 0:
            break
        a, b = data[idx*2+1], data[idx*2]
        if a > b:
            data[idx] = b
        else:
            data[idx] = a
 

# AOJ DSL_2_A
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_A

N, Q = map(int, input().split())
data = [2**31-1] * (2*N+1)

for _ in range(Q):
    q, x, y = list(map(int, input().split()))
    if q == 0:
        update(x, y)
    else:
        print(query(x, y+1))
