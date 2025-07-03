# Challenge Day 22

import argparse

#  Step 1: Set up the argument parser
parser = argparse.ArgumentParser(description="Convert temperature between Celsius and Fahrenheit.")

#  Step 2: Add command-line arguments
parser.add_argument("temperature",type=float,help="Temperature value to convert")
parser.add_argument("unit",choices=["C", "F"],help="Target unit: C for Celsius, F for Fahrenheit")

#  Step 3: Parse arguments
args = parser.parse_args()
temp = args.temperature
target_unit = args.unit.upper()

#  Step 4: Conversion logic
if target_unit == "C":
    converted_temp = (temp - 32) * 5 / 9
    print(f"{temp:.2f}°F is equal to {converted_temp:.2f}°C")
elif target_unit == "F":
    converted_temp = (temp * 9 / 5) + 32
    print(f"{temp:.2f}°C is equal to {converted_temp:.2f}°F")
