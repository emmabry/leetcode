# Given a string s containing just the characters '(' ')' '{' '}' '[' ']', 
# determine if the input string is valid.
# Open brackets must be closed by the same type of brackets, in correct order
# Every closed bracker has a corresponding open bracket of the same type

# Initial Solution
def isValid(s):
    stack = []
    for i in s:
        try:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                    stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        except IndexError:
            return False
    return len(stack) == 0

# Refined Solution
def isValid(s):
    hashmap = {')': '(', ']': '[','}': '{'}
    stack = []
    for i in s:
        if i in hashmap:
            if not stack or hashmap[i] != stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append()
    return len(stack) == 0
