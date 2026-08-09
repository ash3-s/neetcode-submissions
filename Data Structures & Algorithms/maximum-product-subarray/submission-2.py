class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            r = nums[i]
            for j in range(len(nums)):
                if j > i:
                    r *= nums[j]
                res = max(res, r)
        return res