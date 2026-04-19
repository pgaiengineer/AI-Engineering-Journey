'''
Write a program with two functions:

1. celsius_to_fahrenheit(c): Takes a Celsius value and returns Fahrenheit (F = C * 9/5 + 32).

2. check_safety(temp): Takes a temperature (in Fahrenheit) and returns 
"SAFE" if it's under 100 or "DANGER" if it's over.

The Flow:
1. Ask the user for a Celsius temperature.
2. Use the first function to convert it.
3. Use the second function to check the safety of that converted result.
4. Print the final status.
'''

##### My Solution #####
# Create functions
def celsius_to_fahrenheit(C):
    F = C * 9 / 5 + 32
    return F

def check_safety(temp):
    if temp < 100:
        return "SAFE"
    else:
        return "DANGER"

# Create user interaction
temp_in_celsius = float(input("Enter a temperature in °C: "))

# Execute functions
temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)
is_safe = check_safety(temp_in_fahrenheit)

# Print output
print(f"temperature status = {is_safe}")


##### Gemini Solution #####
def convert_temp(c):
    return (c * 9/5) + 32

def get_status(f_temp):
    if f_temp > 100:
        return "DANGER: Overheating"
    else:
        return "System Stable"

# Main Program
user_c = float(input("Enter Lab Temperature in Celsius: "))
f_result = convert_temp(user_c)
status = get_status(f_result)

print(f"Temperature is {f_result}F. Status: {status}")