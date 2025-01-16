
# O(2^n) - Exponential Time Complexity
# This function has a time complexity of O(2^n) because it generates all possible subsets of the input set.
# The number of subsets of a set with n elements is 2^n, where n is the size of the input set.
# As the value of n increases, the number of subsets generated increases exponentially.
# The time taken by the function to execute is proportional to 2 raised to the power of the input size n.
# The time complexity of this function is O(2^n) or exponential time complexity.
# The subset generation problem is an example of a problem with exponential time complexity.
# The subset generation problem involves generating all possible subsets of a given set.
def generate_subsets(arr):
    subsets = []
    n = len(arr)
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(arr[j])
        subsets.append(subset)
    return subsets

arr = [1, 2, 3]
subsets = generate_subsets(arr)
print("Subsets:", subsets)
# Output: Subsets: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# This function generates all possible subsets of the input set arr using a binary representation of numbers.
# The function iterates over all numbers from 0 to 2^n - 1, where n is the size of the input set arr.
# For each number, the function generates a subset by considering the binary representation of the number.
# If the j-th bit of the number is set, the j-th element of the input set arr is included in the subset.
# The function generates all possible subsets of the input set by iterating over all numbers from 0 to 2^n - 1.
# The time complexity of this function is O(2^n), where n is the size of the input set arr.
# The function has an exponential time complexity because the number of subsets generated is 2^n, where n is the size of the input set.
# As the value of n increases, the number of subsets generated increases exponentially.
# The time taken by the function to execute is proportional to 2 raised to the power of the input size n.
# The time complexity of this function is O(2^n) or exponential time complexity.