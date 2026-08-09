class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, index)
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stack.append((h, start))
        
        for h, i in stack:
            maxArea = max(maxArea, (len(heights) - i)*h)
        return maxArea

