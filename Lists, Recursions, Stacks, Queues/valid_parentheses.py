def isValid(s):

    # Create a dictionary of valid parentheses
    valid_parentheses = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    # Create a stack to store the parentheses
    stack = []

    # Iterate through the string
    for char in s:

        # If the character is a valid opening parenthesis, push it to the stack
        if char in valid_parentheses:
            stack.append(char)

        # If the character is a valid closing parenthesis, pop the stack and compare
        # the popped character to the current character
        elif stack and char == valid_parentheses[stack[-1]]:
            stack.pop()

        # If the character is not a valid opening or closing parenthesis, return False
        else:
            return False

    # If the stack is empty, return True
    return not stack


# test case
s = "()[]{}"
print(isValid(s))

# test case
s = "([)]"
print(isValid(s))