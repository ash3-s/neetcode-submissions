class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = 1
        nums.sort()
        numset = set(nums)
        for i in range(1, len(numset)+1):
            if s in numset:
                s += 1
        return s
