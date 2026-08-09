class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict, coldict, squaredict = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowdict[r] or board[r][c] in coldict[c] or board[r][c] in squaredict[(r//3,c//3)]:
                    return False
                rowdict[r].add(board[r][c])
                coldict[c].add(board[r][c])
                squaredict[(r//3,c//3)].add(board[r][c])
        return True




