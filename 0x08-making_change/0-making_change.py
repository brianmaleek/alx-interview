#!/usr/bin/python3
"""
Coin Change Algorithm
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        - coins (list of int): A list of coin values available.
        - total (int): The target total amount to achieve.

    Returns:
    int:
        - The fewest number of coins needed to meet the total amount.
        - If the total amount cannot be met by any combination of coins,
            returns -1.
        - If the total is 0 or less, returns 0.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order to check the largest coins first
    coins.sort(reverse=True)

    num_coins = len(coins)
    min_coins = 0
    coin_index = 0

    # Iterate through the coins
    while coin_index < num_coins and total > 0:
        # Check if the current coin can be used
        if coins[coin_index] <= total:
            total -= coins[coin_index]
            min_coins += 1
        else:
            coin_index += 1

    # If total cannot be met by any combination of coins, return -1
    if total > 0:
        return -1

    return min_coins
