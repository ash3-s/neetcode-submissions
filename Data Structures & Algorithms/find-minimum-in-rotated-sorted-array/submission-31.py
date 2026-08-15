class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[0]
        while l <= r:
            mid = (l + r) // 2
            print(nums[mid])
            if nums[mid] <= nums[0]:
                # right sorted
                if nums[mid] < nums[-1]:
                    r = mid - 1
                else:
                    l = mid + 1
                minVal = min(minVal, nums[mid])
            else:
                l = mid + 1
                



        return minVal