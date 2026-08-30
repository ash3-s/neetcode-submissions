class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(arr):
            rob1, rob2 = 0, 0

            for n in arr:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(houseRobber(nums[1:]), houseRobber(nums[:-1]),nums[0])
