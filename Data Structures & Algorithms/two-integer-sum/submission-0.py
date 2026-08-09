class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,v in enumerate(nums):
            val = target - v
            if val in hashmap:
                return [hashmap[val],i]
            hashmap[v] = i
        