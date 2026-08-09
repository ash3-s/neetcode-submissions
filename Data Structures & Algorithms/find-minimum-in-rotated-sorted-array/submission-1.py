class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        res = nums[r]
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > res:
                l = mid + 1
            else:
                res = min(res,nums[mid])
                r = mid - 1

        return res