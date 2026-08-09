class Solution:
    def findMin(self, nums: List[int]) -> int:
        minEl = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if nums[m] >= nums[0]:
                l = m + 1
            else: 
                r = m - 1

            
            minEl = min(nums[m], minEl)
        return minEl
