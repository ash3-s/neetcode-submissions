class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []
        for i in s:
            if i in mapping.values():
                stack.append(i)
            else:
                if stack and stack[-1] == mapping[i]: 
                    stack.pop()
                else: 
                    return False
        return len(stack) == 0