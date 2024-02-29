#!/usr/bin/python3
'''
This module implements a functon that shows an algorithm
to determine the fewest number of coins needed to meet a
given amount.
'''
def makeChange(coins, total):
    if total == 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: It takes 0 coins to make amount 0

    # Iterate over each coin value
    for coin in coins:
        # Update dp array for each possible amount from coin value to total
        for amount in range(coin, total + 1):
            # Calculate the minimum number of coins needed to make the current amount
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if the total amount can be made with the available coins
    return dp[total] if dp[total] != float('inf') else -1
