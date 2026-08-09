class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0
        maxArea = 0
        maxLeft = []
        maxRight = []
        l, r = 0, len(height) - 1

        a = 0
        for i in height:
            maxLeft.append(a)
            a = max(a,i)

        b = 0
        for i in range(len(height)-1,-1,-1):
            maxRight.append(b)
            b = max(b,height[i])
        maxRight = maxRight[::-1]  
        for i in range(len(height)):
            area = min(maxLeft[i],maxRight[i]) - height[i]
            if area > 0:
                maxArea += area

        return maxArea

