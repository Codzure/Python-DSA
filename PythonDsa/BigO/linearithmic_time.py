# O(n log n) - Linearithmic Time Complexity
# This function has a time complexity of O(n log n) because it has a loop that runs n times and performs a binary search operation in each iteration.
# The binary search operation has a time complexity of O(log n), and it is performed n times in the loop.
# As the value of n increases, the number of binary search operations increases logarithmically, resulting in a total time complexity of O(n log n).
# The time taken by the function to execute is proportional to the product of the input size n and the logarithm of the input size.
# The time complexity of this function is O(n log n) or linearithmic time complexity.
# Merge sort is an example of an algorithm with linearithmic time complexity.
# Merge sort is a sorting algorithm that divides the input array into two halves, recursively sorts the two halves, and then merges the sorted halves.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
# Output: Sorted array: [3, 9, 10, 27, 38, 43, 82]
# This function implements the merge sort algorithm to sort an input array in ascending order.
# The merge sort algorithm divides the input array into two halves, recursively sorts the two halves, and then merges the sorted halves.
# The time complexity of the merge sort algorithm is O(n log n), where n is the size of the input array.
# The merge sort algorithm has a linearithmic time complexity because it divides the input array into two halves and performs merge operations in each iteration of the recursion.
# The time taken by the function to execute is proportional to the product of the input size n and the logarithm of the input size.
# The time complexity of this function is O(n log n) or linearithmic time complexity.
