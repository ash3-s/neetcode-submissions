class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = []

        for p, s in zip(position, speed):
            time.append([p, (target-p)/s])
        time.sort()
        stack = [time[-1][1]]
        # print(time[::-1])
        for p, t in time[::-1]:
            if stack and stack[-1] < t:
                stack.append(t)
        return len(stack)