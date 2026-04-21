'''
Write a program that:

1. Creates an empty list called lab_records.

2. Uses a loop to collect data for 2 samples.

3. For each sample, ask for the Name and the pH level.

4. Create a dictionary for that sample: {"name": name, "ph": ph_level}.

5. Append that dictionary to your lab_records list.

6. Finally, loop through the list and print: "Sample [Name] has a pH of [pH]."
'''
# Create an empty list
lab_records = []

# Record sample data
for i in range(2):
    name = input("Enter sample name: ")
    ph_level = float(input("Enter sample pH level: "))
    # print(f"{name}, {ph_level}")

    # Store sample data in dictionaries
    sample = {
        "name": name,
        "ph": ph_level
    }

    # Store each dictionary in the list
    lab_records.append(sample)
    # print(lab_records)

# Print out the records
for record in lab_records:
    print(f"Sample {record['name']} has a pH of {record['ph']}.")