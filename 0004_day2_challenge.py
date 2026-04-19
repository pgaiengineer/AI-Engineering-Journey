'''
1. Write a program that asks for a chemical's pH level (0 to 14).

2. If the pH is less than 7, print: "The substance is Acidic. Handle with gloves."

3. If the pH is exactly 7, print: "The substance is Neutral. It is likely water."

4. If the pH is greater than 7, print: "The substance is Basic/Alkaline. Handle with caution."

5. Bonus: Add a check to see if the user entered a number outside of 0-14 and print "Invalid pH level."
'''

# Get the pH of the chemical and convert the input to a float
chemical_pH = float(input("What is the pH of the chemical (pH must be between 0 to 14): "))

# Check if input is within range
if chemical_pH < 0 or chemical_pH > 14:
    print("Invalid pH level")

# Implement core Logic
elif chemical_pH < 7:
    print("The substance is Acidic. Handle with gloves.")
elif chemical_pH == 7:
    print("The substance is Neutral. It is likely water.")
else:
    print("The substance is Basic/Alkaline. Handle with caution.")