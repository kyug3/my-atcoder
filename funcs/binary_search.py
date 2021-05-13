def is_ok(idx, key):
    # 条件を満たす最大のindexを求める
    if lst[idx] > key:
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

# lst = [1, 14, 32, 51, 51, 222]
# print(binary_search((51)))
# 5