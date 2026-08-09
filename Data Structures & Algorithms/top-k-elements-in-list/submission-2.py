class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums)+1)]
        countdict = defaultdict(int)

        for i in nums:
            countdict[i] += 1
        
        for key, v in countdict.items():
            freq[v].append(key)
        
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
