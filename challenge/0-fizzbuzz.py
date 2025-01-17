#!/usr/bin/python3
""" FizzBuzz Implementation
"""
import sys


def fizzbuzz(limit):
    """
    FizzBuzz function prints numbers from 1 to `limit` separated by a space.

    - For multiples of 3, prints "Fizz" instead of the number.
    - For multiples of 5, prints "Buzz" instead of the number.
    - For multiples of both 3 and 5, prints "FizzBuzz".
    """
    if limit < 1:
        return

    results = []  # List to store FizzBuzz results
    for num in range(1, limit + 1):
        if num % 15 == 0:  # Check if divisible by both 3 and 5
            results.append("FizzBuzz")
        elif num % 3 == 0:  # Check if divisible by 3
            results.append("Fizz")
        elif num % 5 == 0:  # Check if divisible by 5
            results.append("Buzz")
        else:
            results.append(str(num))  # Add the number as a string
    print(" ".join(results))  # Print all results in a single line


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Error: Missing number")  # Clearer error message
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    try:
        number = int(sys.argv[1])  # Convert input to integer
        fizzbuzz(number)
    except ValueError:  # Handle cases where input is not a valid integer
        print("Error: Input must be a valid integer")
        sys.exit(1)
