#!/usr/bin/python3
'''
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
'''


def makeChange(coins, total):
    """
    makeChange: returns fewest coins number needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
