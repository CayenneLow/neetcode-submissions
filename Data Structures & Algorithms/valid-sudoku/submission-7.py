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
                if not self.helper(row_seen_map, row, num):
                    return False
                # Mark col
                if not self.helper(col_seen_map, col, num):
                    return False
                # Mark cell
                cell = ((row)//3, (col)//3)
                if not self.helper(cell_seen_map, cell, num):
                    return False
        return True
    
    def helper(self, seen_map: Dict, key: int | tuple[int,int], num: str) -> bool:
        if key not in seen_map:
            seen_map[key] = {}
        if num in seen_map[key]:
            return False
        seen_map[key][num] = True
        return True