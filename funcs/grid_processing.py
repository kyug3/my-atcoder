def rot90(A):
    return list(zip(*(A[::-1])))
    
def rm_extra(A, rem='.'):
    for _ in range(4):
        A = rot90(A)
        while all(x == rem for x in A[-1]):
            A.pop()
    return A
