class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = {}
        col_seen = {}
        cell_seen = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                if num == ".":
                    continue
                cell = (row//3, col//3)
                if row not in row_seen:
                    row_seen[row] = set()
                if col not in col_seen:
                    col_seen[col] = set()
                if cell not in cell_seen:
                    cell_seen[cell] = set()
                if (num in row_seen[row]) or (num in col_seen[col]) or (num in cell_seen[cell]):
                    return False 
               
                row_seen[row].add(num)
                col_seen[col].add(num)
                cell_seen[cell].add(num)
        return True