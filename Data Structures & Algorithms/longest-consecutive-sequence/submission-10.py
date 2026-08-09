class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)
        for n in numset:
            longest = 0
            if n-1 in numset:
                continue
            while n in numset:
                longest += 1
                n += 1
            res = max(longest,res)
        return res

                
            
            