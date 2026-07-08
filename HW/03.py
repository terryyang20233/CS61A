def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3

    """
    "*** YOUR CODE HERE ***"
    if n == 0: # 选取0作为首项
        return 0
    else:
        return num_eights(n // 10) + (n % 10 == 8)



def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16

    """
    "*** YOUR CODE HERE ***"
    if n < 10: #选取任何个位数作为首项，否则个位数//10再取模10必为0，把首位数直接计算进去了
        return 0
    else:
        return abs((n % 10) - ((n // 10) % 10)) + digit_distance(n // 10)



def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28

    """
    "*** YOUR CODE HERE ***"
    def even_or_odd(n):
        if n == 1:
            return True
        else:
            return not even_or_odd(n-1)


    if n == 1:
        return odd_func(1)
    else:
        return interleaved_sum(n-1, odd_func, even_func) + even_or_odd(n)*odd_func(n) + (1-even_or_odd(n))*even_func(n)


''' One alternative version here
    def sum_from(k):
        if k > n:
            return 0
        elif k == n:
            return odd_func(k)
        else:
            return odd_func(k) + even_func(k+1) + sum_from(k + 2) # 每次跳过两层，避开奇偶问题
    return sum_from(1)

'''

''' Another alternative version here
    def helper(k, f1, f2):
        if k > n:
            return 0
        # 当前数字 k 永远套用 f1，下一层让 k+1，并将 f1 和 f2 互换位置！
        return f1(k) + helper(k + 1, f2, f1)
        
    return helper(1, odd_func, even_func)

'''
