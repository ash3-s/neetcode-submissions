class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        minL = float("infinity")
        for r in range(len(nums)):
            if sum(nums[l:r+1]) >= target:
                minL = min(minL, r-l+1)
                while sum(nums[l:r+1]) >= target:
                    minL = min(minL, r-l+1)
                    l += 1
        return minL if minL != float("infinity") else 0
                
                
            
