class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        stack = []
        for c in s:
            if stack and c in openToClose and openToClose[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            print(stack)
        return len(stack) == 0

