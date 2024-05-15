#!/usr/bin/python3
"""prime game
"""

def isWinner(x, nums):
  """
  This function determines the winner of a game where players take turns
  choosing prime numbers and removing them and their multiples from a set.

  Args:
      x: The number of rounds of the game.
      nums: An array of integers representing the starting set for each round.

  Returns:
      A string indicating the winner ("Maria" or "Ben") or None if the winner 
      cannot be determined.
  """

  maria_wins = 0
  ben_wins = 0
  for num in nums:
    # Check if the number itself is prime (corner case for n=1)
    if num == 1:
      ben_wins += 1
      continue

    # Track whose turn it is (Maria starts)
    turn = "Maria"
    while True:
      # Find the smallest prime factor of the current number
      prime_factor = find_prime_factor(num)

      # Remove the prime factor and its multiples
      num = remove_multiples(num, prime_factor)

      # Check if the number is reduced to 1
      if num == 1:
        if turn == "Maria":
          ben_wins += 1
        else:
          maria_wins += 1
        break

      # Switch turns
      turn = "Ben" if turn == "Maria" else "Maria"

  # Determine the winner based on win count
  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None

def find_prime_factor(num):
  """
  This helper function finds the smallest prime factor of a number.

  Args:
      num: The number to find the prime factor for.

  Returns:
      The smallest prime factor of the number.
  """
  # Iterate through potential prime factors (2 is always the first prime)
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return i
  return num  # num itself is prime

def remove_multiples(num, prime):
  """
  This helper function removes the prime factor and its multiples from a number.

  Args:
      num: The number to remove multiples from.
      prime: The prime factor to remove.

  Returns:
      The number with multiples of the prime factor removed.
  """
  while num % prime == 0:
    num //= prime
  return num

# Example usage
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

