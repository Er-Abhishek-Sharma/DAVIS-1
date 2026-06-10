# Function to calculate factorial of a number
def factorial(n):
    # Check if the number is negative
    if n < 0:
        print("Factorial is not defined for negative numbers")
    
    # Factorial of 0 or 1 is 1
    elif n == 0 or n == 1:
        return 1
    
    else:
        # Initialize result to 1
        result = 1
        # Loop from 2 to n (inclusive) to calculate factorial
        for i in range(2, n + 1):
            result *= i  # Multiply result by the current number
        return result  # Return the final factorial value

# Ask user to enter a number
number = int(input("Enter a number to calculate its factorial: "))

# Print the factorial of the entered number
print("The factorial of", number, "is", factorial(number))
