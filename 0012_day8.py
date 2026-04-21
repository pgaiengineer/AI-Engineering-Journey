# A python dictionary stores objects in key value pairs
# Keys are hashed to determine where in memory they are stored

# Create a dictionary

user = {
    "name": "Alice",
    "age": 25,
}
print(user)

# Access a value using the key
print(user["name"])
# or
print(user.get("name"))  # this method is safer since it returns NONE if no key is found

# Update a value
user["age"] = 26
print(user)

# Add a new key-value pair
user["city"] = "New York"
print(user)

# Merge with another dictionary or iterable key-value pair
user.update({"status": "active", "level": 5})
print(user)

# Iterate and view
print(user.keys())  # list-like view of keys
print(user.values())  # list-like view of values
print(user.items())  # list-like view of key-value pairs as tuples

# Membership
print("age" in user)  # check if key in dictionary

# Length
print(len(user))  # number of key-value pairs

# Remove items
print(user.pop("level"))  # removes the key and returns the value
print(user)

print(user.popitem())  # removes and returns last inserted key-value pair
print(user)

del user["city"]  # removes key-value pair with no return
print(user)