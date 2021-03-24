N = int(input())

def sum_of_arithmetic_sequence(n, a = 1, d = 1):
    """
    Args:
        n int: the number of terms
        a int: the first term
        d int: the common difference
    
    Return:
        int: sum of arithmetic sequence
    """
    return n * (2 * a + (n - 1) * d) // 2

print(sum_of_arithmetic_series(N - 1))