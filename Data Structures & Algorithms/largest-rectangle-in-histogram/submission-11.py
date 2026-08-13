class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, start)

        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, ind = stack.pop()
                maxArea = max(maxArea, (i-ind) * height)
                start = ind 

            stack.append((h, start))
        
        for h, i in stack:
            maxArea = max(maxArea, (len(heights) - i)*h)
        return maxArea