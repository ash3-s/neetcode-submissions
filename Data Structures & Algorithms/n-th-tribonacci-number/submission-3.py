class Solution:
    def tribonacci(self, n: int) -> int:
        a, b ,c = 0, 1, 1
        for i in range(n - 2):
            tempc = c
            tempb = b
            c = c + b + a
            b = tempc
            a = tempb
        return c if n > 0 else 0