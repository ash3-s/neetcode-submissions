class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = set()

        for i in nums:
            if i in hashmap:
                return i
            hashmap.add(i)
        
