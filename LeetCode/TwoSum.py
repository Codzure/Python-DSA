from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
    
# # Test cases
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
# print(sol.twoSum([3, 2, 4], 6))  # Output: [1, 2]
# print(sol.twoSum([3, 3], 6))  # Output: [0, 1]

# Time complexity: O(n^2)
# Space complexity: O(1)

# The brute-force solution has a time complexity of O(n^2) because we have two nested loops iterating over the input list.
# The space complexity is O(1) since we are using a constant amount of space to store the loop indices.
# While this solution works, it is not the most efficient approach for solving the Two Sum problem, especially for large input sizes.
# This will allow us to reduce the time complexity to O(n) and improve the overall performance of the algorithm

# We can optimize the solution by using a hash table to store the indices of the elements we have seen so far.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the numbers we've seen so far and their indices
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the hash table
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store the current number and its index in the hash table
            seen[num] = i
        
        return []


    # Test cases
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sol.twoSum([3, 2, 4], 6))  # Output: [1, 2]
print(sol.twoSum([3, 3], 6))  # Output: [0, 1]

# Time complexity: O(n)
# Space complexity: O(n)

# The optimized solution has a time complexity of O(n) because we iterate through the input list once, and each lookup in the hash table takes O(1) time.
# The space complexity is O(n) because we store at most n elements in the hash table.

# The optimized solution is more efficient than the brute-force approach, especially for large input sizes, as it reduces the time complexity from O(n^2) to O(n).
# This makes it a better choice for solving the Two Sum problem in practice.
