class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsdict, colsdict, squaresdict = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowsdict[r] or board[r][c] in colsdict[c] or board[r][c] in squaresdict[(r//3,c//3)]:
                    return False
                rowsdict[r].add(board[r][c])
                colsdict[c].add(board[r][c])
                squaresdict[(r//3,c//3)].add(board[r][c])
        return True