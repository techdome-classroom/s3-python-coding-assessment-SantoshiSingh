class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to hold the values of Roman numerals
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0

        # Iterate over the Roman numeral string from right to left
        for char in reversed(s):
            current_value = roman_to_int[char]
            
            # If the current value is less than the previous value, we subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Update the previous value for the next iteration
            prev_value = current_value

        return total


if __name__ == "__main__":
    # Taking user input for the Roman numeral
    user_input = input()

    # Creating an instance of Solution class
    solution = Solution()

    # Converting Roman numeral to integer and printing the result
    result = solution.romanToInt(user_input)
    print( result)
