class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, ind = stack.pop()
                area = (i - ind) * height
                res = max(res, area)
                start = ind
            stack.append((h, start))
            
        for h, i in stack:
            res = max(res, h * (len(heights) - i))
        return res