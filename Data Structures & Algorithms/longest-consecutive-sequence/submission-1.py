class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset  = set(nums)
        maxLen = 0
        for i in numset:
            longest = 0
            num = i
            if i -1 in numset:
                continue
            while num in numset:
                num +=1 
                longest += 1
            maxLen = max(maxLen,longest)
        return maxLen


