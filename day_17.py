# Challenge Day 17

# Build a context manager for safe file handling

# Using class:

# Define a custom context manager class for safe file reading
class Safe_File_Read:
    def __init__(self, filename, mode):
        # Store filename and mode (e.g., 'r' for read, 'w' for write)
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        # This method runs when entering the 'with' block
        print(f"Opening {self.filename} .........")
        # Open the file and store the file object
        self.file = open(self.filename, self.mode)
        # Return the file object so it can be used inside the 'with' block
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        # This method runs automatically after the 'with' block finishes,
        # even if an error occurs
        print(f"Closing {self.filename} .........")
        # Close the file to free system resources
        self.file.close()

# Use the custom context manager to open and read a file safely
with Safe_File_Read("my_file.txt", "r") as f:
    # 'f' is the opened file object returned by __enter__()
    data = f.read()  # Read the entire content of the file
    print(f"Reading content of the file:\n{data}")

# This line runs after the 'with' block — file is already closed at this point
print("File Closed")
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Using Context Manager Decorator

# Import the contextmanager decorator to create a context manager using a generator
from contextlib import contextmanager

# Define a function-based context manager using the @contextmanager decorator
@contextmanager
def safe_file_read(filename, mode):
    try:
        # Setup part: open the file and print a message
        print(f"Opening {filename} .........")
        f = open(filename, mode)
        # Yield the file object to the 'with' block
        yield f
    finally:
        # Cleanup part: this will run no matter what (even if an error occurs)
        print(f"Closing {filename} .........")
        f.close()

# Use the custom context manager to read a file safely
with safe_file_read("my_file.txt", "r") as f:
    # 'f' is the file object returned by yield
    data = f.read()
    print(f"Reading content of the file:\n{data}")

# This runs after the 'with' block. The file is already closed.
print("File Closed")
