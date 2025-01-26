import array as arr

# Importing the array module

# Creating an array of integers
numbers = arr.array('i', [1, 2, 3, 4, 5])

# Display the array
print("Array:", numbers[:]) # Output: Array: array('i', [1, 2, 3, 4, 5])

# Accessing elements
print("First element:", numbers[0])
print("Second element:", numbers[1])

# Adding elements
numbers.append(6)
print("Array after append:", numbers)

numbers.extend([7, 8, 9]) # Adding multiple elements
print("Array after extend:", numbers)

numbers.insert(0, 0) # Inserting element at the beginning
print("Array after insert:", numbers)

# Removing elements
numbers.remove(3) # Removing element 3
print("Array after remove:", numbers)

popped_element = numbers.pop() # Removing the last element
print("Popped element:", popped_element)
print("Array after pop:", numbers)

# Slicing the array
print("Sliced array (2 to 5):", numbers[2:5])

# Looping through the array
print("Looping through the array:")
for num in numbers:
    print(num, end=' ')
print()

# Finding the index of an element
index = numbers.index(4)
print("Index of element 4:", index)

# Reversing the array
numbers.reverse() # Reversing the array
print("Array after reverse:", numbers)

# Getting the buffer info
print("Buffer info:", numbers.buffer_info())

# Counting occurrences of an element
count = numbers.count(2)
print("Count of element 2:", count)

# Converting array to a list
numbers_list = numbers.tolist()
print("Array converted to list:", numbers_list)


# Time Complexity of Array Operations:
# 	•	Accessing an element: O(1) (constant time complexity)
# 	•	Searching an element: O(n) (linear search) (linear time complexity)
# 	•	Insertion/Deletion: O(n) (due to shifting elements) (linear time complexity)
# 	•	Space Complexity: O(n) where n is the number of elements in the array. (linear space complexity)

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

arr = [10, 20, 30, 40, 50]
print(sum_array(arr))  # Output: 150