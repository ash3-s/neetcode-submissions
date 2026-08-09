class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        output = [[] for i in range((len(nums) + 1))] 
        for n in nums:
            hashmap[n] += 1

        for key, val in hashmap.items():
            output[val].append(key)

        res = []
        for i in range(len(output) - 1, - 1, -1):
            for j in output[i]:
                res.append(j)
                if len(res) == k:
                    return res

