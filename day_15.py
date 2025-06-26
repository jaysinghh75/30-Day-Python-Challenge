# Challenge Day 15

import time  # Import the time module to measure execution time

# Define the decorator to measure and log the time a function takes
def time_log(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Start the timer
        result = func(*args, **kwargs)  # Call the original function with all its arguments
        end = time.time()  # End the timer
        print(f"Time taken to read the file: {(end - start) * 1000:.2f} ms")  # Print the time in milliseconds
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# Apply the time_log decorator to the reading function
@time_log
def reading(filename):
    # Open the file and read its contents
    with open(filename, 'r') as f:
        text = f.read()
        return text  # Return the text content of the file

# Call the function with the file name
reading("my_file.txt")
