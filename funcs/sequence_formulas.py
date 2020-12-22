def sum_of_arithmetic_sequence(n, a = 1, d = 1):
    """
    Args:
        n int: the number of terms
        a int: the first term
        d int: the common difference
    
    Return:
        int: the sum of arithmetic sequence
    """
    return n * (2 * a + (n - 1) * d) // 2

def sum_of_geometric_sequence(n, a = 1, r = 2):
    """
    Args:
        n int: the number of terms
        a int: the first term
        r int: the constant ratio

    Return:
        int: the sum of geometric sequence
    """
    return a * (1 - r ** n) // (1 - r)
