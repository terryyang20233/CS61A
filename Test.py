def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    "*** YOUR CODE HERE ***"
    # Recursive version happy happy happy
    # what about this 
    # if n==1:
    #     return f
    # return lambda x: f(make_repeater(f, n-1)(x))

    def repeat(x)  
        k = 1 
	while k <= n:
            k, x = k+1, f(x)
        return x

    return repeat


