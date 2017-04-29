# -*- coding: utf-8 -*-

def find_integer_divisors(n):
    # Check input ...
    if n <= 2:
        # Return answer ...
        return []

    # Create empty list ...
    ans = []

    # Loop over possible divisors ...
    for i in xrange(2, 1 + n / 2):
        # Check if it is valid ...
        if n % i == 0:
            ans.append(i)

    # Return answer ...
    return ans
