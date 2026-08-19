class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
            if x < y:
                heapq.heappush(stones, (y - x) * -1)
            elif x > y:
                heapq.heappush(stones, (x - y) * -1)
            else:
                continue
        return abs(stones[0]) if stones else 0
            



