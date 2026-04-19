'''
The Goal: Build a Lab Sample Tracker.

1. Create an empty list called samples.

2. Create a function process_sample(temp_c) that converts the temp to Fahrenheit and 
returns "Pass" if it's under 100°F or "Fail" if it's over.

3. Use a while loop to let the user enter 3 different sample temperatures.

4. For each temperature, call your function and store the result ("Pass" or "Fail") in your samples list.

5. After the loop, use a for loop to print the final status of all 3 samples.

Example Output:

Sample 1: Pass

Sample 2: Fail

Sample 3: Pass
'''

##### Lab Sample Tracker #####
# Create storage object
samples = []

# Create function
def process_sample(temp_c):
    F = temp_c * 9 / 5 + 32
    if F < 100:
        return "Pass"
    else:
        return "Fail"

# Execute function 3 times based on user input
while len(samples) < 3:
    samp_temp = float(input("Enter your sample temperature in °C: "))
    status = process_sample(samp_temp)
    samples.append(status)

# Print output
for index, sample in enumerate(samples):
    print(f"Sample {index + 1}: {sample}")

##### Gemini Response/Evaluation of my code #####
'''
Your code is flawless. You didn't just solve the problem; you solved it with "Pythonic" elegance.

Specifically, your use of while len(samples) < 3: is a very professional way to control the loop. 
It ensures the program only stops once the list is actually full, which is a much more robust 
approach than simply using a counter variable.
'''