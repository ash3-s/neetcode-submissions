class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = []

        openToClose = {
            ']' : '[',
            '}' : '{',
            ')':'(',
        }

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                # if stack:
                    if stack and stack[-1] == openToClose[i]:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
