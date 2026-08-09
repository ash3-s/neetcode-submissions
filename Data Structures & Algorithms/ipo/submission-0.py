class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minHeap = [(c, p) for c,p in zip(capital, profits)]
        heapq.heapify(minHeap)

        for i in range(k):

            while minHeap and minHeap[0][0] <= w:
                c , p =  heapq.heappop(minHeap)
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)
        return w