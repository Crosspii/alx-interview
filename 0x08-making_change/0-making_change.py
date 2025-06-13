#!/usr/bin/python3
"""Making Change coin interview question."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to make a given amount."""
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
