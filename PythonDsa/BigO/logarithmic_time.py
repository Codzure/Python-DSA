# O(log n) - Logarithmic Time Complexity
# This function has a time complexity of O(log n) because it divides the input size n by 2 in each iteration of the loop.
# As the value of n increases, the number of iterations of the loop increases logarithmically.
# The time taken by the function to execute is proportional to the logarithm of the input size n.
# The time complexity of this function is O(log n) or logarithmic time complexity.
# Binary search is an example of an algorithm with logarithmic time complexity.
# Binary search is a search algorithm that finds the position of a target value within a sorted array.
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
index = binary_search(arr, target)
print("Index of element", target, ":", index)
# Output: Index of element 5 : 4
# This function implements the binary search algorithm to find the index of a target element in a sorted array.
# The binary search algorithm divides the array into two halves and compares the target element with the middle element of the array.
# If the target element is equal to the middle element, the index of the middle element is returned.
# If the target element is less than the middle element, the search is restricted to the left half of the array.
# If the target element is greater than the middle element, the search is restricted to the right half of the array.
# This process is repeated until the target element is found or the search space is exhausted.
# The time complexity of the binary search algorithm is O(log n), where n is the size of the input array.
# The binary search algorithm has a logarithmic time complexity because it divides the search space in half in each iteration of the loop.

