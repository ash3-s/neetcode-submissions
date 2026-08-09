class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsdict, colsdict, squaresdict = defaultdict(list), defaultdict(list), defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowsdict[r] or board[r][c]  in colsdict[c] or board[r][c] in squaresdict[(r//3,c//3)]:
                    return False
                rowsdict[r].append(board[r][c])
                colsdict[c].append(board[r][c])
                squaresdict[(r//3,c//3)].append(board[r][c])
        return True