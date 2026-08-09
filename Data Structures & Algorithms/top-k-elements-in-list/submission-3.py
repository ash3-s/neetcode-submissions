class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        arr = [[] for i in range(len(nums)+1)]
        res = []
        for i in nums:
            count[i] += 1
        
        for key, val in count.items():
            arr[val].append(key)
        for i in range(len(arr)-1, -1, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res

