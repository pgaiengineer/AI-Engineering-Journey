# A basic function to calculate a dilution
def calculate_dilution(c1, v1, c2):
    # c1*v1 = c2*v2 -> v2 = (c1*v1)/c2
    v2 = (c1 * v1) / c2
    return v2

# Now call the function
required_volume = calculate_dilution(10, 5, 2)
print(f"You need to dilute to {required_volume}mL")