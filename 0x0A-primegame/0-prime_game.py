#!/usr/bin/python3
"""Prime Game
"""


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner of each round in the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the ranges for each round.

    Returns:
        str or None: The name of the player that won the most rounds.
        If the winner cannot be determined, returns None.
    """
    # Function to find the next prime number in the set
    def find_next_prime(current, nums):
        for i in range(current + 1, len(nums)):
            if is_prime(nums[i]):
                return nums[i]
        return -1

    # Main game logic
    winners = {'Maria': 0, 'Ben': 0}

    for n in nums:
        # Counting the number of primes in the given range
        primes_count = sum(1 for num in range(1, n + 1) if is_prime(num))

        # If the number of primes is even, Ben wins. Otherwise, Maria wins.
        if primes_count % 2 == 0:
            winners['Ben'] += 1
        else:
            winners['Maria'] += 1

    # Determining the winner with the most wins
    if winners['Maria'] == winners['Ben']:
        return None
    elif winners['Maria'] > winners['Ben']:
        return 'Maria'
    else:
        return 'Ben'
