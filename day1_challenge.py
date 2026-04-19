'''
    Write a program that: 
    1. Asks the user for their weight in pounds.
    2. Converts that weight to kilograms (kg = lbs / 2.2).
    3. Calculates a protein target (1.6g of protein per kg of body weight).
    4. Prints the result clearly.
'''
# 1. Input (Inputs always come in as Strings, so we 'wrap' them in float())
weight_lbs = float(input("Enter your weight in lbs: "))

# 2. Calculation
weight_kg = weight_lbs / 2.2
protein_goal = weight_kg * 1.6

# 3. Output
print(f"Based on a weight of {weight_lbs}lbs...")
print(f"Your daily protein goal is {protein_goal:.2f} grams.")