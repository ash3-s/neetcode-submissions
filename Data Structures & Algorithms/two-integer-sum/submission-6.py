class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            num = target - n
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[n] = i
        
            