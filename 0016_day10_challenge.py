'''
The Challenge:

1. Ask the user for a sample ID (e.g., "  lab-001  ").

2. Clean it: Remove the spaces and make it all uppercase ("LAB-001").

3. Ask the user for the chemical name (e.g., "ethanol").

4. Clean it: Make it "Title Case" ("Ethanol").

5. Store these in a dictionary and print the final, "Clean" record.
'''

# cleaner functions
def id_cleaner(entry):
    return entry.strip().upper()

def chem_name_cleaner(entry):
    return entry.title()

# storage function
def store(id, chemical):
    return {id: chemical}

# user inputs
sample_id = input("Enter sample ID: ")
chemical_name = input("Enter chemical name: ")

# function execution
inventory = store(id_cleaner(sample_id), chem_name_cleaner(chemical_name))

# print output
for key, value in inventory.items():
    print(f"{key} - {value}")


# Gemini challenge review
'''
This is a fantastic evolution of your coding style. You are now moving into Functional Programming—the 
practice of breaking down every task into small, specialized "workers" (functions).

What you did exceptionally well:
Separation of Concerns: You didn't just "clean" the data; you created dedicated cleaners for IDs 
versus chemical names. This is exactly how production systems handle different data types 
(e.g., a phone number cleaner vs. an email cleaner).

Nested Function Calls: In the line inventory = store(id_cleaner(sample_id), ... ), you "piped" 
the output of one function directly into another. This is an advanced move that keeps code concise.

One Small Engineering Note:
Your store function currently creates a new dictionary every time it runs. If you were to 
put this in a loop to collect 10 samples, inventory would only ever hold the last one entered 
because it overwrites the variable each time.

To keep a running list of your cleaned data, you would usually append that dictionary to a List, 
like we did on Day 6.
'''