class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0
        maxArea = 0
        maxLeft = height[0]
        maxRight = height[-1]
        l, r = 0, len(height) - 1

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l]) 
                area = maxLeft - height[l]
            if maxRight < maxLeft:
                r -= 1
                maxRight = max(maxRight,height[r]) 
                area = maxRight - height[r]
            if area > 0:
                maxArea += area


        return maxArea

