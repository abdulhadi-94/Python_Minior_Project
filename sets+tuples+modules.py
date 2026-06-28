import random
import math

try:
    # Store unique numbers in a set
    numbers = set()

    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.add(num)

    # Convert set to tuple
    numbers_tuple = tuple(numbers)

    print("\nUnique Numbers (Tuple):", numbers_tuple)

    # Pick 3 random numbers
    if len(numbers_tuple) >= 3:
        random_numbers = random.sample(numbers_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Not enough unique numbers to pick 3 random values.")

    # Square root of the sum of tuple elements
    total = sum(numbers_tuple)

    if total >= 0:
        print("Square Root of Sum:", math.sqrt(total))
    else:
        print("Square root cannot be calculated because the sum is negative.")

except ValueError:
    print("Invalid input! Please enter integers only.")

except Exception as e:
    print("An error occurred:", e)