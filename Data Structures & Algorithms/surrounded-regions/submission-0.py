class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or board[r][c] == "X":
                return
            
            board[r][c] = "T"
            visit.add((r,c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == COLS - 1 or r == ROWS - 1 or c == 0) and board[r][c] == "O":
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "T":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

                    