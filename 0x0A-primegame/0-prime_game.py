#!/usr/bin/python3
'''
Main Module for Prime game.
'''


def isWinner(x, nums):
    """ Determine the winner of each game."""

    if x > 0:
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
            if n <= 1:
                # If n is 0 or 1, there are no prime numbers, so Ben wins
                ben_wins += 1
            else:
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
    return None
