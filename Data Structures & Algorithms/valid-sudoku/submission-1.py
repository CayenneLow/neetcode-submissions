class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen_map = {}
        col_seen_map = {}
        cell_seen_map = {} # tuple (0,0) -> {}
        for (row, row_nums) in enumerate(board):
            for (col, num) in enumerate(row_nums):
                if num == ".":
                    continue
                # Mark row
                if row not in row_seen_map:
                    row_seen_map[row] = {}
                if num in row_seen_map[row]:
                    return False
                row_seen_map[row][num] = True
                # Mark col
                if col not in col_seen_map:
                    col_seen_map[col] = {}
                if num in col_seen_map[col]:
                    return False
                col_seen_map[col][num] = True
                # Mark cell
                cell = ((row)//3, (col)//3)
                if cell not in cell_seen_map:
                    cell_seen_map[cell] = {}
                if num in cell_seen_map[cell]:
                    print(f"Duplicate found in {cell}. num: {num}. State: {cell_seen_map}")
                    return False
                cell_seen_map[cell][num] = True
        return True