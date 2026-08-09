class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people) - 1
        boats = 0
        while l <= r:
            remaining = limit - people[r]
            r -= 1
            boats += 1
            if l <= r and people[l] <= remaining:
                l += 1

        return boats

