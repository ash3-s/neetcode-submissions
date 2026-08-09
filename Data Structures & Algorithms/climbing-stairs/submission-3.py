class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        cache = {}
        for i in range(n-1):
            if i in cache:
                return cache[i]
            temp = one
            one = one + two 
            two = temp
            cache[i] = one
        return one