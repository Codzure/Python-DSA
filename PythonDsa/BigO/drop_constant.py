# Drop constant factors and lower order terms
# O(2n) -> O(n)

def print_items_twice(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(i,j)
print_items_twice(3)

# This function has a time complexity of O(n) because the number of iterations of the loops is directly proportional to the input size n.
# The function has two loops, each of which runs n times.
# The time taken by the function to execute is directly proportional to the input size n.
# The time complexity of the function is O(n) because the function has two loops that run n times each.
# The time complexity of this function is O(n) or linear time complexity.

# output:
# 0
# 1
# 2
# 0
# 1
# 2
# The function prints the numbers from 0 to n-1 twice, once in each loop.
# The function has two loops, each of which runs n times, resulting in a total of 2n iterations.

#More examples:
# O(n + 10) -> O(n)
# O(n^2 + 5n + 10) -> O(n^2)
# O(100n^2 + 5n + 10) -> O(n^2)
# O(1) -> O(1)
# O(100) -> O(1)
# O(n^3 + n^2 + n + 10) -> O(n^3)
# O(n^2 + n log n + n) -> O(n^2)
# O(n log n + n) -> O(n log n)


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_items(10)
