
# Initialize a list
numbers = [2, 4, 1, 9, 7, 5]

# Determine the number of elements in a list
print(len(numbers))

# Checking the list for emptiness
if not numbers:
  print("List is empty")
else:
  print("List is not empty")

# Find the highest and lowest values in a list
print("Max value:", max(numbers))
print("Min value:", min(numbers))

# Delete a list item with a given value
value_to_delete = 9
numbers.remove(value_to_delete)
print("List after removing", value_to_delete, ":", numbers)
