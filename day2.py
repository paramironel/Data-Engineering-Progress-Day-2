# Step 1: Create a new file day2_datatypes.py
# Step 2: Declare different data types

integer_var = 10
float_var = 10.5
string_var = "Hello, World!"
boolean_var = True
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3)
set_var = {1, 2, 3}
dict_var = {"name": "Alice", "age": 30}

# Step 3: Print the data types
print("Integer:", integer_var, "Type:", type(integer_var))
print("Float:", float_var, "Type:", type(float_var))
print("String:", string_var, "Type:", type(string_var))
print("Boolean:", boolean_var, "Type:", type(boolean_var))
print("List:", list_var, "Type:", type(list_var))
print("Tuple:", tuple_var, "Type:", type(tuple_var))
print("Set:", set_var, "Type:", type(set_var))
print("Dictionary:", dict_var, "Type:", type(dict_var))

# Step 4: Convert types
number_str = "100"
number_int = int(number_str)
print("Converted String on Integer:",number_int, "Type:", type(number_int))

