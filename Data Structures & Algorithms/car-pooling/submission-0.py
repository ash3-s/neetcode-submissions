class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        minHeap = []
        countPass = 0
        for t in trips:
            numPass, start, end = t
            while minHeap and minHeap[0][0] <= start:
                countPass -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            countPass += numPass
            if countPass > capacity:
                return False
            heapq.heappush(minHeap, [t[2], t[0]])
        
        return True

