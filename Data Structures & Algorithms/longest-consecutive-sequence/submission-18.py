class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numset = set(nums)
        for n in numset:
            if n - 1 in numset:
                continue
            length = 0
            while n in numset:
                length += 1
                maxLen = max(maxLen, length)
                n += 1
        return maxLen
