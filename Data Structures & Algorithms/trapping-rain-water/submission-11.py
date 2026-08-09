class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxArea = 0
        while l <= r:
            if maxL < maxR:
                area = maxL - height[l]
                maxL = max(maxL, height[l])
                l += 1
            else:
                area = maxR - height[r]
                maxR = max(maxR, height[r])
                r -= 1
            if area > 0:
                maxArea += area
        return maxArea