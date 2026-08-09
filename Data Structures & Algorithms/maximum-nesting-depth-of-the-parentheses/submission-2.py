class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        depth = 0
        for c in s:
            if c == "(":
                stack.append(c)
                maxDepth += 1
                depth = max(depth, maxDepth)
            elif c == ")":
                stack.pop()
                maxDepth -= 1
            else: continue
        return depth