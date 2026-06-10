"""To create a program to print all the even factors of a given number by creating a function"""

def even_factorial(n):
    """
    Function to calculate the product of all even numbers up to n.
    For example, if n = 6, even numbers are 2, 4, 6 → product = 48
    """
    even_fact = 1  # Initialize result
    
    # Loop through all even numbers from 2 up to n
    for i in range(2, n + 1, 2):
        even_fact *= i  # Multiply the result by the current even number
    
    return even_fact  # Return the final even factorial

# Ask user to enter a number
number = int(input("Enter a number to calculate its even factorial: "))

# Print the even factorial of the entered number
print("The even factorial of", number, "is", even_factorial(number))


