# program1.py
class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold matching pairs
        matching_brackets = {')': '(', '}': '{', ']': '['}

        # Stack to store opening brackets
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in matching_brackets:
                # Pop from stack if there's a matching opening bracket
                top_element = stack.pop() if stack else '#'
                if matching_brackets[char] != top_element:
                    return False
            else:
                # Push opening bracket to the stack
                stack.append(char)

        # Return True if the stack is empty, else False (handles cases like "")
        return not stack
