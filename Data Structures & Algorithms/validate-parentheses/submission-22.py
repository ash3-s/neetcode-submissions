class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        stack =[]

        for c in s:
            if c in ["]", "}", ")"] and stack and openToClose[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return False if len(stack) else True