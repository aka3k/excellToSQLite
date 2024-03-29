import random as rnd
import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def generate_random_prime_numbers(n, max_iterations=1000):
    prime_numbers = []
    attempts = 0

    while len(prime_numbers) < n and attempts < max_iterations:
        num = rnd.randint(1, 10000)
        if is_prime(num):
            prime_numbers.append(num)
        attempts += 1

    return prime_numbers

n = 5
print(generate_random_prime_numbers(n))