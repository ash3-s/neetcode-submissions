class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addFruit(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] == 0:
                return
            
            q.append((r,c))
            visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        hour = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                addFruit(r, c + 1)
                addFruit(r + 1, c)
                addFruit(r, c - 1)
                addFruit(r - 1, c)
            hour += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return hour if hour != -1 else 0
            