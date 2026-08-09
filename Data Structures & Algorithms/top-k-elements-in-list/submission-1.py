class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        res = []
        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1
        
        for keyy,v in hashmap.items():
            freq[v].append(keyy)

        for i in range(len(freq)-1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res