class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Create a dictionary to store the values of the Roman numerals
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the result variable to store the integer value of the Roman numeral
        result = 0
        
        # Iterate through the input string
        for i in range(len(s)):
            # Get the value of the current Roman numeral
            value = roman_dict[s[i]]
            
            # If the next Roman numeral exists and its value is greater than the current value
            if i + 1 < len(s) and roman_dict[s[i + 1]] > value:
                # Subtract the current value from the result
                result -= value
            else:
                # Add the current value to the result
                result += value
        
        return result
    

    # Test cases
sol = Solution()
print(sol.romanToInt("III"))  # Output: 3
print(sol.romanToInt("IV"))  # Output: 4
print(sol.romanToInt("IX"))  # Output: 9
print(sol.romanToInt("LVIII"))  # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
print(sol.romanToInt("MMMCMXCIX"))  # Output: 3999

# Time complexity: O(n), where n is the length of the input string s.
# Space complexity: O(1). The space used by the dictionary roman_dict is constant.
