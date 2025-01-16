# Create a function that takes an array of numbers and returns the sum of the numbers.



def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total  # Correctly returns total without any issue.


# Time complexity: O(n)
# Space complexity: O(1)

print(sum_array([1, 2, 3, 4, 5]))  # Output: 15