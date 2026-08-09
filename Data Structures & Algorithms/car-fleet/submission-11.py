class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p,s) for p,s in zip(position,speed)]

        arr.sort(key = lambda x: x[0])
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            pos, speed = arr[i]
            time = (target - pos) / speed
            if not stack or (stack and stack[-1] < time):
                stack.append(time)
        return len(stack)