class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = nums[::]
        for i in nums:
            n.append(i)
        return n