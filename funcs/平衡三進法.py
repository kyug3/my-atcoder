def pow_three(N):
    """
    平衡三進法
    [3^0, 3^1, 3^2...]
    からいくつか選んで適切に和差を取ると
    任意の整数 N を表現できる
    """
    x = 1
    ret = []
    while N:
        if N % 3 == 0:
            pass
        elif N % 3 == 1:
            ret.append(x)
            N -=1
        else:
            ret.append(-x)
            N += 1
        N //= 3
        x *= 3
    return ret