'''
Imagine you have a batch of 5 chemical samples. You need to record their temperatures. 
If a sample is above 30°C, it's "Unstable." If it's 30°C or below, it's "Stable."

Write a program that:

1. Uses a for loop to run exactly 5 times.

2. Inside the loop, asks the user for a temperature.

3. Uses if/else logic to determine if it is "Stable" or "Unstable."

4. Prints the result for that specific sample.
'''

# Set up the loop. Note the range
for i in range(1, 6):
    # Get the temperature of the sample
    sample_temperature = float(input(f"Enter the temperature of sample {i}: "))
    
    # Add control flow
    if sample_temperature > 30:
        print(f"Sample {i} is unstable")
    else:
        print(f"Sample {i} is stable")

# End the program        
print("Program ended.")