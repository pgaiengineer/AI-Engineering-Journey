# List are wrapped in square brackets []
samples = ["Water", "Ethanol", "Saline", "Acid"]

# Accessing items. (Python starts counting at 0!)
print(samples[0])  # Prints: Water
print(samples[2])  # Prints: Saline

##### Common Operations #####

# Add an item
samples.append("Buffer")
print(samples)

# Number of items in a list
print(len(samples))

# Change an item in a list
samples[1] = "Methanol"
print(samples)

##### Loop through a list #####
results = [22.5, 25.1, 18.9, 31.0]

for temp in results:
    print(f"Reading recorded: {temp}°C")  # use alt + 0176 to get the ° symbol