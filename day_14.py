# Challenge Day 14

# - Calculate factorial recursively

# Define a recursive function to calculate the factorial of a number
def fact(n):
    # Base case: factorial of 0 or 1 is always 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * fact(n - 1)

# Take input from the user
num = int(input("Enter the number to find its factorial: "))

# Call the factorial function and print the result
print(f'The factorial of {num} is {fact(num)}')
