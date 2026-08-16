class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow = nums[0]
        # fast = nums[0]
        i = 0
        while i < len(nums):
            slow = nums[i]
            fast = nums[nums[i]]
            if slow == fast:
                break
            i += 1
        return slow