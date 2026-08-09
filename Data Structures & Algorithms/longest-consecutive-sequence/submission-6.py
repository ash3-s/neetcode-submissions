class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for i in numset:
            length = 1
            if i-1 in numset:
                continue
            while i+1 in numset:
                length += 1
                i += 1
            res = max(res,length)
        return res
