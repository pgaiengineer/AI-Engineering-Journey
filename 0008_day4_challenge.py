'''
Write a program that:

1. Starts with an empty list called inventory.

2. Uses a while loop to ask the user to "Enter a supply name" (e.g., Beaker, Pipette, Slides).

3. Type "quit" to stop adding items.

4. After the loop finishes, use a for loop to print the final inventory list, but count 
the items as you print them
'''

inventory = []

while True:
    supply_name = input("Enter a supply name or type quit to print list: ")
    if supply_name != "quit":
        inventory.append(supply_name)
        # print(inventory)
    else:
        for index, item in enumerate(inventory):
            print(f"{index + 1}- {item}")
        break  # exits the loop and ends the script execution

##### Gemini Solution #####
inventory = []
active = True

while active:
    item = input("Add to inventory (or type 'quit'): ")
    if item.lower() == "quit":
        active = False
    else:
        inventory.append(item)

print("\n--- Final Lab Inventory ---")
for index, item in enumerate(inventory):
    print(f"{index + 1}. {item}")