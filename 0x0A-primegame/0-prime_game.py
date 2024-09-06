#!/usr/bin/python3
"""
Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds."""
    if x < 1 or not nums:
        return None

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(max_num**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, max_num + 1, start):
                is_prime[multiple] = False

    marias_wins = 0
    bens_wins = 0

    for num in nums:
        prime_count = sum(is_prime[:num])
        if prime_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
