class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        target = 0
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] + a < target:
                    j += 1
                elif nums[j] + nums[k] + a > target:
                    k -= 1
                else:
                    res.append([nums[j], nums[k], a])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res
