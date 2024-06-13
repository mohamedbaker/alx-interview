#!/usr/bin/python3
'''
    minimum operations task challenge.
'''

def minOperations(n):
    """
    Calculates the minimum number of operations (Copy All, Paste)
      needed to achieve n H characters.
    Args:
        n: The target number of H characters.
    Returns:
        int: The minimum number of operations required, or 0 if impossible.
    """

    if n <= 1:
        return 0

    memo = {}

    def helper(n):
        if n in memo:
            return memo[n]

        # Base case
        if n == 1:
            return 0

        min_ops = float('inf')

        for i in range(2, n + 1):
            if n % i == 0:
                min_ops = min(min_ops, helper(n // i) + i)

        memo[n] = min_ops
        return min_ops

    return helper(n)
