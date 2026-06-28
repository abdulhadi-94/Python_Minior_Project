import math
import random
from datetime import datetime

# Dictionary to store history
history = {}


# Function for Basic Arithmetic
def basic_arithmetic():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose operation: ")

        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            result = num1 / num2
        else:
            print("Invalid Choice!")
            return None

        print("Result:", result)
        return result

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid number entered.")
    return None


# Function for Scientific Calculations
def scientific_calculation():
    try:
        print("\n1. Square Root")
        print("2. Power")
        print("3. Factorial")

        choice = input("Choose operation: ")

        if choice == "1":
            num = float(input("Enter number: "))
            result = math.sqrt(num)

        elif choice == "2":
            base = float(input("Enter base: "))
            power = float(input("Enter exponent: "))
            result = math.pow(base, power)

        elif choice == "3":
            num = int(input("Enter number: "))
            result = math.factorial(num)

        else:
            print("Invalid Choice!")
            return None

        print("Result:", result)
        return result

    except ValueError:
        print("Invalid Input!")
    except Exception as e:
        print("Error:", e)
    return None


# Function for Random Numbers
def generate_random():
    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        result = random.randint(start, end)
        print("Random Number:", result)
        return result

    except ValueError:
        print("Invalid Input!")
    return None


# Function to Store Result
def store_result(result):
    if result is not None:
        timestamp = str(datetime.now())
        history[timestamp] = result
        print("Result stored successfully.")


# Function to View History
def view_history():
    if len(history) == 0:
        print("No history available.")
    else:
        print("\n------ History ------")
        for time, result in history.items():
            print(f"{time} --> {result}")


# Main Menu
while True:
    print("\n====== SMART CALCULATOR & DATA MANAGER ======")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Number")
    print("4. Store Last Result")
    print("5. View History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if "last_result" not in locals():
        last_result = None

    if choice == "1":
        last_result = basic_arithmetic()

    elif choice == "2":
        last_result = scientific_calculation()

    elif choice == "3":
        last_result = generate_random()

    elif choice == "4":
        store_result(last_result)

    elif choice == "5":
        view_history()

    elif choice == "6":
        print("Thank you for using Smart Calculator!")
        break

    else:
        print("Invalid Choice! Please try again.")