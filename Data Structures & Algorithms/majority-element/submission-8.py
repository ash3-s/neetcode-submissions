class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        for k, v in hashmap.items():
            if v > math.floor((len(nums))/2):
                return k
        
