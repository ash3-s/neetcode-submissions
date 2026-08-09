class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset  = set(nums)
        maxLen = 0
        for i in numset:
            longest = 0
            num = i
            if i -1 not in numset:
                while num in numset:
                    num +=1 
                    longest += 1
            else:
                continue
            maxLen = max(maxLen,longest)
        return maxLen


