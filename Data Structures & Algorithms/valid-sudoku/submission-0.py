class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(rows+cols)
        # Validate rows first
        for row in board:
            seen_map = {}
            for num in row:
                if num == ".":
                    continue
                if num in seen_map:
                    print(f"Duplicate number {num}")
                    return False
                seen_map[num] = True
            
        # O(rows+cols)
        seen_map_by_col = {}
        for (row, row_nums) in enumerate(board):
            for (col, num) in enumerate(row_nums):
                if num == ".":
                    continue
                if col not in seen_map_by_col:
                    seen_map_by_col[col] = {}
                if num in seen_map_by_col[col]:
                    print(f"Duplicate number {num}")
                    return False
                seen_map_by_col[col][num] = True

        cell_seen_map = {} # tuple (0,0) -> {}
        for (row, row_nums) in enumerate(board):
            for (col, num) in enumerate(row_nums):
                if num == ".":
                    continue
                cell = ((row)//3, (col)//3)
                if cell not in cell_seen_map:
                    cell_seen_map[cell] = {}
                if num in cell_seen_map[cell]:
                    print(f"Duplicate found in {cell}. num: {num}. State: {cell_seen_map}")
                    return False
                cell_seen_map[cell][num] = True

        return True