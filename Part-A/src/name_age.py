"""This program calculates a person's birth year from their age.

Input:
    The name is entered by the user as a string.
    The age is entered by the user as an integer. 

Process:
    The person's age is subtracted from the current year to calculate their birth year.

Output:
    A string containing the person's name and birth year is displayed in the terminal/screen.

Typical usage example:
    What is your name? Nicole
    How old are you? 28
    Hello Nicole! You were born in 1998.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name?\n")
    age = int(input("How old are you?\n"))

    birth_year = CURRENT_YEAR - age
    
    print(f"Hello {name}! You were born in {birth_year}.")
    


# === Main Guard ===
if __name__ == "__main__":
    main()

