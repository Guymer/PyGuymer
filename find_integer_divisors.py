# -*- coding: utf-8 -*-

##############################################################################################
#                  This file is deprecated because Python 2.x is deprecated                  #
#                     A Python 3.x version of this file can be found at:                     #
#                                                                                            #
# https://github.com/Guymer/PyGuymer3/blob/master/find_integer_divisors.py                   #
##############################################################################################

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
