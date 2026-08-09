class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for v, w in edges[n1]:
                if v not in visit:
                    heapq.heappush(minHeap, (w + w1, v))
        return t if len(visit) == n else -1




