class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev = None
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            
            count, char = heapq.heappop(maxHeap)
            res += char
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if count != 0:
                prev = [count, char]
        return res