class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []
        for p in points:
            distance = math.sqrt(p[0]**2 + p[1]**2)
            d.append([distance, p])
        heapq.heapify(d)
        print(d)
        j = 0
        res = []
        while True:
            h = heapq.heappop(d)
            res.append(h[1])
            j += 1
            if j == k:
                return res 
