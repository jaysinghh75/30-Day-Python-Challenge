# Challenge Day 11

from datetime import date
from dateutil.relativedelta import relativedelta  # For calculating age in years, months, days

# Function to calculate and display age
def find_my_age():
    try:
        # Ask user to enter date of birth in YYYY-MM-DD format
        dob = date.fromisoformat(input("Enter your DOB in (YYYY-MM-DD) format: "))
    except ValueError:
        # If user enters invalid format, show error message
        print("Error: Please enter the DOB in this format (YYYY-MM-DD)")
    else:
        curr_date = date.today()  # Get today's date
        age = relativedelta(curr_date, dob)  # Calculate difference in years, months, days
        print(f'You are {age.years} years, {age.months} months and {age.days} days old')

# Function to calculate days left until next birthday
def birthday_countdown():
    try:
        # Ask user to enter their date of birth
        dob = date.fromisoformat(input("Enter your DOB in (YYYY-MM-DD) format: "))
    except ValueError:
        # Show error if format is incorrect
        print("Error: Please enter the DOB in this format (YYYY-MM-DD)")
    else:
        curr_date = date.today()  # Get today's date

        # Create a date for upcoming birthday in the current year
        upcoming_birthday = dob.replace(year=curr_date.year)

        # If this year's birthday has already passed, shift to next year
        if curr_date > upcoming_birthday:
            upcoming_birthday = upcoming_birthday.replace(year=upcoming_birthday.year + 1)

        # Calculate the number of days remaining
        countdown = upcoming_birthday - curr_date 
        print(f"{countdown.days} days are left in your birthday")

# Ask user what they want to do
choices = input("What do you want to know:\nChoose 1 to know your age\nChoose 2 to know your birthday countdown\n")

# Use match-case to handle the choice (Python 3.10+)
match choices:
    case "1":
        find_my_age()  # Call function to calculate age
    case "2":
        birthday_countdown()  # Call function to calculate birthday countdown
    case _:
        print("Invalid choice!!")  # Handle invalid input
