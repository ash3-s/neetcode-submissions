class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0

        
        time = []
        stack = []
        arr = []
        for p, s in zip(position,speed):
            t = (target - p) / s
            time.append(t)

        for p, t in zip(position, time):
            arr.append((p,t))
        arr.sort()
        for i in range(len(arr)-1, -1, -1):
            stack.append(arr[i])
            res += 1
            if len(stack) >= 2 and stack[-1][1] <= stack[-2][1]:
                stack.pop()
                res -= 1
        return res
            
        
        

        