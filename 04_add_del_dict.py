# Write a python code to add and delete element from a dictionary using functions

my_dict = {"name": "Sachin", "age": 19, "city": "Rupnagar"}
print(f"Dictionary: {my_dict}")

print("Add element to the dictionary: ")
key = input("Enter key: ")
value = input("Enter value: ")
my_dict[key] = value
print(f"Added {key}: {value} to the dictionary.")
print(f"Dictionary: {my_dict}")

print("Delete element from the dictionary: ")
key = input("Enter key: ")
if key in my_dict:
  value = my_dict.pop(key)
  print(f"Deleted {key}: {value} from the dictionary.")
  '''Or use:
  del my_dict(key)
  print(key is deleted)
  '''
else:
  print(f"{key} is not in the dictionary")

print(f"Dictionary: {my_dict}")