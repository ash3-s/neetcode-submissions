class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        i = 0
        while True:
            num = heapq.heappop(nums)
            i += 1
            if i == k:
                return -num