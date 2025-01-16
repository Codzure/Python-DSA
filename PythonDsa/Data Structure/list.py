# big o of list
# Accessing an element in a list by index: O(1)
# Appending an element to a list: O(1)
# Removing an element from a list: O(n)
# Inserting an element into a list: O(n)
# Searching for an element in an unsorted list: O(n)
# Searching for an element in a sorted list: O(log n)
# Iterating over a list: O(n)
# Slicing a list: O(k)
# Extending a list: O(k)
# Sorting a list: O(n log n)
# Reversing a list: O(n)
# Copying a list: O(n)
# Creating a list: O(n)
# List comprehension: O(n)
# List concatenation: O(n)
# List repetition: O(n)
# List length: O(1)
# List contains: O(n)
# List index: O(n)
# List min/max: O(n)
# List element assignment: O(1)
# List element deletion: O(n)


my_list = [1, 2, 3, 4, 5] # O(1)
print(my_list[0]) # O(1)
print(my_list[1]) # O(1)

# The time complexity of accessing an element in a list by index is O(1) because it takes a constant amount of time to access an element in a list, regardless of the size of the list.
# The time taken to access an element in a list is independent of the size of the list, and the time complexity is O(1) or constant time complexity.
# Constant time complexity indicates that the time taken to access an element in a list is constant and does not depend on the size of the list.


my_list.append(6) # O(1)
print(my_list) # O(1) # output: [1, 2, 3, 4, 5, 6]
my_list.pop(0) # O(1)
print(my_list) # O(1) # output: [2, 3, 4, 5, 6]

my_list.insert(0, 10) # O(n) 
print(my_list) # O(1) # output: [1, 2, 3, 4, 5, 6]