class Solution:
    def trap(self, height: List[int]) -> int:
        # water that can be trapped in position i -> min(maxL, maxR) - height[i]
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxArea = 0
        while l <= r:
            if maxL < maxR:
                maxL = max(maxL, height[l])
                area = maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                area = maxR - height[r]
                r -= 1
            maxArea += area
        return maxArea
