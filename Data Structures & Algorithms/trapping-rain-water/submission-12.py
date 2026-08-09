class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0

        l, r = 0, len(height) - 1
        maxArea = 0
        while l <= r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL < maxR:
                maxArea += maxL - height[l] 
                l += 1
            else:
                maxArea += maxR - height[r]
                r -= 1
        return maxArea