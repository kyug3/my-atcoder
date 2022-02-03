def is_ok(x):
    if x:
        return 1
    else:
        return 0

def binary_search():
    ng = -1
    ok = 10**18 + 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

# lst = [1, 14, 32, 51, 51, 222]
# print(binary_search((51)))
# 5