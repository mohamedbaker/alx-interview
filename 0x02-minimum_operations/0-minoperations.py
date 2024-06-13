#!/usr/bin/python3
def minOperations(n, memo={}):
  """
  Calculates the minimum number of operations (Copy All, Paste) needed to achieve n H characters.
  Args:
      n: The target number of H characters.
      memo (dict, optional): Memoization table to store minimum operations for subproblems. Defaults to {}.
  Returns:
      int: The minimum number of operations required, or 0 if impossible.
  """

  if n == 0:
    return 0
  elif n == 1:
    return 1

  if n in memo:
    return memo[n]

  min_ops = float('inf')
  for j in range(1, n // 2 + 1):
    remaining_ops = minOperations(n - j, memo)
    operations = 1 + remaining_ops
    min_ops = min(min_ops, operations)

  memo[n] = min_ops

  return min_ops
