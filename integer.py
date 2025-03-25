#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 25, 2025
"""
This program checks whether an integer entered
by the user is positive, negative, or zero.
"""


def main():
    # Get the integer that the user entered.
    entered_int = int(input("Enter an integer.\n"))

    # Check if the user entered an integer greater than zero.
    if entered_int > 0:
        # Display that the integer is a positive integer.
        print(f"\n{entered_int} is a positive integer.")
    # Check if the user entered an integer less than zero.
    elif entered_int < 0:
        # Display that the integer is a negative integer.
        print(f"\n{entered_int} is a negative integer.")
    # Otherwise, the integer has to be zero.
    else:
        # Display that zero is just zero.
        print("\nZero is just zero.")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
