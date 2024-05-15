#!/usr/bin/python3
"""Prime Game
"""


def isPrime(num):
    """isPrime
    @param num: int
    @return: bool
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """isWinner
    @param x: int
    @param nums: list
    @return: int
    """
    def play_game(n):
        """play_game
        @param n: int
        @return: bool
        """
        primes = [i for i in range(2, n + 1) if isPrime(i)]
        player = 0
        while primes:
            prime = primes.pop(0)
            if (n // prime) * prime == n:
                player = 1 - player
        return "Maria" if player == 0 else "Ben"

    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = play_game(n)
        wins[winner] += 1
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
