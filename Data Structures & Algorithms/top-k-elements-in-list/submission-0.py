class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        countdict = defaultdict(int)
        arr = [[] for _ in range(len(nums)+1)]
        for i in nums:
            countdict[i] += 1
        
        for keyy,v in countdict.items():
            arr[v].append(keyy)
        for i in range(len(arr)-1, -1, -1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res) == k:
                    return res
                
