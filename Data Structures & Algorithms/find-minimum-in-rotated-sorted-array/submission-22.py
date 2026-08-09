class Solution:
    def findMin(self, nums: List[int]) -> int:
        minEl = float("inf")

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if nums[m] > nums[0] and nums[m] < nums[-1]:
                # minEl = min(nums[m], minEl)
                r = m - 1
            elif nums[m] >= nums[0] and nums[m] > nums[-1]:
                # minEl = min(nums[m], minEl)
                l = m + 1
            elif nums[m] < nums[0] and nums[m] < nums[-1]:
                r = m - 1
            else:
                r = m - 1

            
            minEl = min(nums[m], minEl)
        return minEl
