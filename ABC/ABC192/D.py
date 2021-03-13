X = input()
M = int(input())
if len(X) == 1:
    X = int(X)
    if X <= M:
        print(1)
    else:
        print(0)
    exit()

def base_n(x, n):
    x = str(x)
    cnt = 0
    for e, i in enumerate(range(len(x))[::-1]):
        cnt += int(x[i]) * (n ** e)
    return cnt

def is_ok(idx, key):
    if base_n(X, idx) > key:
        return True
    else:
        return False

def binary_search(key):
    ng = -1
    ok = 10 ** 18 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, key):
            ok = mid
        else:
            ng = mid
    return ok - 1

start = int(max(list(X)))
ans = binary_search(M) - start
print(max(0, ans))