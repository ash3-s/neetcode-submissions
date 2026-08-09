class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            num = target - v
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[v] = i
        