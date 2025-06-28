# Challenge Day 16

# Generate the first n Fibonacci numbers with a generator


# Generator function to produce 'n' Fibonacci numbers
def fib_seq(n: int):
    a, b = 0, 1  # Initialize the first two numbers of the Fibonacci sequence
    for _ in range(n):  # Loop 'n' times (we don't need the loop variable, so we use '_')
        yield a         # Yield the current number in the sequence
        a, b = b, a + b # Update 'a' and 'b' to the next two Fibonacci numbers

# Take input from the user
n = int(input("Enter the number: "))

# Print a header before showing the Fibonacci numbers
print(f"The first {n} Fibonacci numbers are:")

# Iterate over the generator and print each Fibonacci number
for f in fib_seq(n):
    print(f)
