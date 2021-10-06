def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1; R >>= 1


def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if not v:
            continue
        lazy[2*i-1] += v; lazy[2*i] += v
        data[2*i-1] += v; data[2*i] += v
        lazy[i-1] = 0


def update(l, r, x):
    # [l, r)に x を足す
    *ids, = gindex(l, r)
    propagates(*ids)

    L = N0 + l; R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] += x; data[R-1] += x
        if L & 1:
            lazy[L-1] += x; data[L-1] += x
            L += 1
        L >>= 1; R >>= 1
    for i in ids:
        data[i-1] = max(data[2*i-1], data[2*i])


def query(l, r):
    # [l, r)の最大を返す
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r

    s = 0
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R-1])
        if L & 1:
            s = max(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

# INF = float('inf')
N = 10 ** 5 + 1
LV = (N-1).bit_length()
N0 = 2 ** LV
data = [0] * (2*N0)
lazy = [0] * (2*N0)


# 区間和、区間最大
# 区間最小にするときは38, 50, 52行のmaxをminにする