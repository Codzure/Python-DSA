# O(n^2) - Quadratic Time Complexity
def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_pairs(3)

# This function has a time complexity of O(n^2) because it has two nested loops.
# The function has two nested loops, where the outer loop runs n times and the inner loop runs n times for each iteration of the outer loop.
# This results in a total of n * n = n^2 iterations of the inner loop.
# As the value of n increases, the number of iterations of the inner loop increases quadratically.
# The time taken by the function to execute is directly proportional to the square of the input size n.
# The time complexity of this function is O(n^2) or quadratic time complexity.