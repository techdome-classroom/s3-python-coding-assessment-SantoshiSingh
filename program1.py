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

        # Return True if the stack is empty, else False
        return not stack


if __name__ == "__main__":
    # Taking user input
    user_input = input()

    # Creating an instance of Solution class
    solution = Solution()

    # Checking if the input string is valid and printing the result
    if solution.isValid(user_input):
        print("True")
    else:
        print("False")
