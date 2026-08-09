class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxArea = 0
        while l < r:
            if maxL > maxR:
                r -= 1
                maxR = max(maxR, height[r])
                water = maxR - height[r]
                maxArea += water
            else:
                l += 1
                maxL = max(maxL,height[l])
                water = maxL - height[l]
                maxArea += water
        return maxArea

                