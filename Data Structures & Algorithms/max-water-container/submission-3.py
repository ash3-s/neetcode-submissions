class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxL, maxR = heights[l], heights[r]
        maxArea = 0
        while l < r:
            if heights[l] < heights[r]:
                area = (r - l ) * heights[l]
                l += 1
            else:
                area = (r - l ) * heights[r]
                r -= 1
            print(area)
            maxArea = max(maxArea, area)
        return maxArea


