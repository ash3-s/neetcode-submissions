class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = [] #(v,i)

        for i,v in enumerate(heights):
            start = i
            if stack and  stack[-1][0] <= v:
                stack.append((v,i))
            
            while stack and stack[-1][0] > v:
                val, ind = stack.pop()
                start = ind
                area = (i - ind) * val
                maxArea = max(maxArea, area)

            stack.append((v,start))
        
        if stack:
            while stack:
                val, ind = stack.pop()
                area = (len(heights) - ind) * val
                maxArea = max(maxArea, area)
        return maxArea

            