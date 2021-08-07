N = int(input())
# N = 配列の長さ
# data[N] が初期配列の 0 に対応する

data = [0] * (2*N+1)

def update(l, r, v):
    # 区間[l, r) に vを足す
    L = l + N
    R = r + N
    while L < R:
        if R % 2 == 1:
            data[R-1] += v
            #data[R-1] %= mod
            r -= 1
        if L % 2 == 1:
            data[L] += v
            #data[L] %= mod
            L += 1
        L //= 2; R //= 2

def query(x):
    # x の総和を求める
    idx = x + N
    ans = data[idx]# % mod
    while True:
        idx //= 2
        if idx == 0:
            break
        ans += data[idx]
        #ans %= mod
    return ans