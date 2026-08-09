class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        n = len(nums)//2
        for i in nums:
            hashmap[i] += 1
        for i, v in hashmap.items():
            if v >= n:
                return i