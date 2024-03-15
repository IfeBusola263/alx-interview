#!/usr/bin/python3
'''
Main Module for Prime game.
'''

# def isPrime(num):
#     """Check if a number is prime."""
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def calculatePrimes(n):
#     """Generate a list of prime numbers up to n."""
#     primes = []
#     for num in range(2, n + 1):
#         if isPrime(num):
#             primes.append(num)
#     return primes

# def isWinner(x, nums):
#     """Determine the winner of each game."""
#     maria_wins = 0
#     ben_wins = 0

#     for n in nums:
#         primes = calculatePrimes(n)
#         # If the number of primes is even, Maria wins, else Ben wins
#         if len(primes) % 2 == 0:
#             maria_wins += 1
#         else:
#             ben_wins += 1

#     # Determine the winner of the most rounds
#     if maria_wins > ben_wins:
#         return "Maria"
#     elif ben_wins > maria_wins:
#         return "Ben"
#     else:
#         return None

def isWinner(x, nums):
    """Determine the winner of each game."""

    def is_prime(num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
