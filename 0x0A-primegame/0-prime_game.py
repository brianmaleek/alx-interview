#!/usr/bin/python3
"""
Module to solve prime game question
"""


def is_prime(n):
    """
    Determine if a number is prime.

    Args:
    - n (int): The number to be checked.

    Returns:
    - bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def calculate_primes_count(n):
    """
    Calculate the number of primes in a range of numbers.

    Args:
    - n (int): The upper limit of the range.

    Returns:
    - int: The number of primes in the range.
    """
    primes_count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            primes_count += 1
    return primes_count


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of a game based on the described
        rules.

    Args:
    - x (int): The number of rounds to be played.
    - nums (list): An array of integers representing n for each round.

    Returns:
    - str or None: The name of the player that won the most rounds. If the
        winner cannot be determined, returns None.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = calculate_primes_count(n)
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
