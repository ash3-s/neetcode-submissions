class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxArea = 0
        while l <= r:
            if maxL < maxR:
                area = maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
            else:
                area = maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])
            maxArea += area
        return maxArea