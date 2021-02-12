def is_ok(idx, key):
    if lst[idx] >= key:
        return True
    else:
        return False

def binary_search(key):
    ng = -1
    ok = len(lst)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, key):
            ok = mid
        else:
            ng = mid
    return ok