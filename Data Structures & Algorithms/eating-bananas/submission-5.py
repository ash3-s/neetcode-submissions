class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = float("inf")
        while l <= r:
            m = (l + r) // 2
            total = 0
            for p in piles:
               total += math.ceil(p/m)
            if total <= h:
                minK = min(minK, m)
                r = m - 1
            else:
                l = m + 1
        return minK

