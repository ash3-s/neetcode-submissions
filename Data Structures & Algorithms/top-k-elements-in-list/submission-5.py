class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = defaultdict(int)
        count = [[] for i in range(len(nums)+1)]
        for i in nums:
            hashmap[i] += 1
        
        for key,value in hashmap.items():
            count[value].append(key)
        
        for i in range(len(count)-1,-1,-1):
            for j in count[i]:
                if len(res) == k:
                    return res
                res.append(j)
        return res