class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0

        def markRotten(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r, c))
            nonlocal fresh
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                markRotten(r + 1, c)
                markRotten(r, c + 1)
                markRotten(r, c - 1)
                markRotten(r - 1, c)
            time += 1
        return time if fresh == 0 else -1