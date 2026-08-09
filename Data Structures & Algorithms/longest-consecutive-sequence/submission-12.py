class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxLen = 0
        for n in numset:
            length = 0
            if n - 1 in numset:
                continue
            while n in numset:
                length += 1
                n += 1
            maxLen = max(maxLen, length)
        return maxLen
            