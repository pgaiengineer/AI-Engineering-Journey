'''
In a lab, stock levels change. Let's practice updating dictionary values.

The Challenge:

1. Create a dictionary called stock with: "Beakers": 10, "Slides": 50, "Gloves": 100.

2. Ask the user which item they used.

3. Ask the user how many they used.

4. Update the dictionary by subtracting that amount.

5. Print the new stock levels using the .items() method in a loop.
'''

# Create the dictionary of the stock
stack = {
    "Beakers": 10,
    "Slides": 50,
    "Gloves": 100
}

# Get the item and amount of item used
item = input("Enter the item you used: ")
# Use if/else to catch any erros
if item in stack.keys():
    amount = int(input("Enter the amount of the item you used: "))

    # Calculate the amount of item left 
    stack[item] -= amount

    # Print the updated stock list
    for key, value in stack.items():
        print(f"{key} - {value}")
else:
    print("Key not found")
    



