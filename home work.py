# 1. Get squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# 2. Extract even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]

# 3. Create a list of tuples (number, square)
squares_tuples = [(x, x**2) for x in range(1, 6)]

# 4. Convert a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]

# 5. Extract vowels from a string
string = "hello world"
vowels = [char for char in string if char in "aeiou"]

# 6. Get numbers divisible by 3 from 1 to 30
divisible_by_3 = [x for x in range(1, 31) if x % 3 == 0]

# 7. Flatten a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested_list for num in sublist]

# 8. Generate a dictionary of squares
squares_dict = {x: x**2 for x in range(1, 6)}

# 9. Replace negative numbers in a list with zero
nums = [-5, 3, -2, 8, -1, 0]
non_negative = [x if x >= 0 else 0 for x in nums]

# 10. Reverse strings in a list
names = ["Alice", "Bob", "Charlie"]
reversed_names = [name[::-1] for name in names]

# Print results
print("Squares:", squares)
print("Even Numbers:", evens)
print("Tuples:", squares_tuples)
print("Uppercase Words:", uppercase_words)
print("Vowels:", vowels)
print("Divisible by 3:", divisible_by_3)
print("Flattened List:", flattened)
print("Squares Dictionary:", squares_dict)
print("Non-Negative List:", non_negative)
print("Reversed Names:", reversed_names)
