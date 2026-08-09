class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1) ]
        
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        
        for key, val in hashmap.items():
            arr[val].append(key)
        
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
