def print_items(a, b):
    for i in range(a): # O(a)
         print(i)

    for j in range(b): # O(b)
            print(j)


print_items(3, 5)
# The time complexity of this function is O(a + b) because the function has two loops, one that runs a times and another that runs b times.
# The time taken by the function to execute is proportional to the sum of a and b.
# The time complexity of this function is O(a + b) or linear time complexity.
# The function prints the numbers from 0 to a-1 and from 0 to b-1 in two separate loops.
# The time taken by the function to execute is proportional to the sum of a and b.
