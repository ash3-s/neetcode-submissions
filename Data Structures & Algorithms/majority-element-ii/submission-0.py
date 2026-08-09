class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        res = []
        for i in nums:
            hashmap[i] += 1
        
        for i in nums:
            if hashmap[i] > len(nums)//3:
                res.append(i)
        return list(set(res))