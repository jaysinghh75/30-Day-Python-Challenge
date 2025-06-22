# Challenge Day 12

import re  # Importing the regular expressions module

# Function to validate a Gmail address
def check_email(email: str):
    # Pattern to ensure email ends with @gmail.com (case-insensitive)
    pattern = '.@gmail\.com$'

    # Pattern to check for invalid structures:
    # \s       - whitespace characters
    # ^\.+     - email starts with a dot
    # \.+@     - dot immediately before @
    # \.{2,}   - two or more consecutive dots
    invalid_pattern = '\s|^\.+|\.+@|\.{2,}'

    # Check if email matches basic Gmail pattern
    if re.findall(pattern, email, flags=re.I):
        # Further check for invalid characters or patterns
        if re.findall(invalid_pattern, email):
            print(f"{email} is Invalid ❌")
        else:
            print(f"{email} is Valid ✅")
    else:
        print(f"{email} is Invalid ❌")

# Take user input and strip leading/trailing whitespaces
email = input("Enter your email to check: ").strip()
check_email(email)
