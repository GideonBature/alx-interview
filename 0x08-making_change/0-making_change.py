#!/usr/bin/python3
"""0. Change comes from within
"""


def makeChange(coins, total):
    """Fewest number of coins needed to meet
    a given amount total

    @param
        coins: list of coins
        total: target amount

    @return
        fewest number of coins needed
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    min_number_of_coins = 0
    total_left = total

    for coin in coins:
        number_of_coin = total_left // coin
        total_left -= number_of_coin * coin
        min_number_of_coins += number_of_coin

    if total_left == 0:
        return min_number_of_coins
    else:
        return -1
