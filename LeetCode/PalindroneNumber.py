class Solution:
    def isPalindrome(self, x: int) -> bool:

        #A palindrome number is a number that is the same when its digits are reversed

        # Check if the number is negative
        if x < 0:
            return False
        

        x_str = str(x)  # Convert the integer to a string
        
        # Check if the string is a palindrome
        return x_str == x_str[::-1] # Compare the string with its reverse
