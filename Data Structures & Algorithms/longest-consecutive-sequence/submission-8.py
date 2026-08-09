class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        maxLen = 0

        for i in nums:
            longest = 0
            if i-1 in numsSet:
                continue
            while i in numsSet:
                longest += 1
                i += 1
            maxLen = max(maxLen, longest)
        return maxLen


