#!/usr/bin/python3
'''
    minimum operations task challenge.
'''
import math


def get_largest_factor(n):
    """
    Returns the largest factor of a number excluding the number itself.
    """

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return n // i
    return 1


def minOperations(n):
    """
    Returns the minimum number of operations required to generate n consecutive
    'H' characters using 'Copy All' and 'Paste' operations.
    """

    memo = {}

    def helper(n):
        if n <= 1:
            return 0

        if n in memo:
            return memo[n]

        largest_factor = get_largest_factor(n)

        if largest_factor == 1:  # n is prime
            memo[n] = n
            return n

        # Calculate the number of operations required
        result = (n // largest_factor) + helper(largest_factor)
        memo[n] = result

        return result

    return helper(n)
