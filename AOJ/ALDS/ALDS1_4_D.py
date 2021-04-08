def is_ok(idx):
    n = 1
    weight = 0
    for i in w:
        weight += i
        if weight > idx:
            n += 1
            weight = i
    if n > k:
        return False
    return True



def binary_search():
    ng = max(w) - 1
    ok = sum(w)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]
print(binary_search())